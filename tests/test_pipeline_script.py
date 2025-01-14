import os
import pathlib
import subprocess

import pytest

from lineapy.api.api_utils import extract_taskgraph
from lineapy.utils.utils import get_system_python_version, prettify


def check_requirements_txt(t1: str, t2: str):
    return set(t1.split("\n")) == set(t2.split("\n"))


@pytest.mark.slow
@pytest.mark.parametrize(
    "artifact_names, dag_name, deps",
    [
        pytest.param(
            ["p value"],
            "sliced_housing_simple",
            {},
            id="sliced_housing_simple",
        ),
        pytest.param(
            ["p value", "y"],
            "sliced_housing_multiple",
            {},
            id="sliced_housing_multiple",
        ),
        pytest.param(
            ["p value", "y"],
            "sliced_housing_multiple_w_dependencies",
            {"y": {"p value"}},
            id="sliced_housing_multiple_w_dependencies",
        ),
    ],
)
def test_slice_pythonscript(artifact_names, dag_name, deps, script_plugin):
    """
    Test the slice produced by script plugin against a snapshot.
    """
    _, task_graph = extract_taskgraph(artifact_names, deps)
    script_plugin.sliced_pipeline_dag(
        dag_name,
        task_graph,
        output_dir="outputs/generated",
    )
    for file_endings in [
        ".py",
        "_script_dag.py",
        "_Dockerfile",
        "_requirements.txt",
    ]:
        path = pathlib.Path("outputs/generated/" + dag_name + file_endings)
        path_expected = pathlib.Path(
            "outputs/expected/" + dag_name + file_endings
        )
        if file_endings == "_requirements.txt":
            assert check_requirements_txt(
                path.read_text(), path_expected.read_text()
            )
        else:
            to_compare = path_expected.read_text()
            if file_endings == "_Dockerfile":
                system_python_version = get_system_python_version()
                to_compare = to_compare.format(
                    python_version=system_python_version
                )
            if file_endings.endswith(".py"):
                to_compare = prettify(to_compare)
            assert path.read_text() == to_compare


@pytest.mark.slow
def test_run_script_dag(virtualenv, tmp_path):
    """
    Verifies that the dags we produce via our to_pipeline. Airflow take too
    long to run and we're mostly skipping during local runs.
    """

    # FIXME - we need a more basic test than this that does not depend on pandas and sklearn etc.
    # installing them takes way too long right now.

    # Copy the dag and the data
    # NOTE: Don't want to leave them in the tests folder, since there are other
    # files we need to copy without which the dag will fail.
    subprocess.check_call(
        [
            "cp",
            "-f",
            "tests/outputs/expected/sliced_housing_multiple_script_dag.py",
            "tests/outputs/expected/sliced_housing_multiple.py",
            "tests/ames_train_cleaned.csv",
            str(tmp_path),
        ]
    )

    os.chdir(str(tmp_path))

    subprocess.check_call(["python", "sliced_housing_multiple_script_dag.py"])
