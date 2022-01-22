import logging
import os
import pathlib
import subprocess
import tempfile
from copy import copy
from typing import List

import click
import rich
import rich.syntax
import rich.tree

from lineapy.data.types import SessionType
from lineapy.db.db import RelationalLineaDB
from lineapy.db.utils import OVERRIDE_HELP_TEXT
from lineapy.exceptions.excepthook import set_custom_excepthook
from lineapy.instrumentation.tracer import Tracer
from lineapy.plugins.airflow import sliced_airflow_dag
from lineapy.transformer.node_transformer import transform
from lineapy.utils.logging_config import configure_logging
from lineapy.utils.utils import prettify

"""
We are using click because our package will likely already have a dependency on
  flask and it's fairly well-starred.
"""

logger = logging.getLogger(__name__)


@click.group()
def linea_cli():
    pass


@linea_cli.command()
@click.option("--db-url", default=None, help=OVERRIDE_HELP_TEXT)
@click.option(
    "--slice",
    default=None,
    multiple=True,  # makes 'slice' variable a tuple
    help="Print the sliced code that this artifact depends on",
)
@click.option(
    "--export-slice",
    default=None,
    multiple=True,  # makes 'export-slice' variable a tuple
    help="Requires --slice. Export the sliced code that {slice} depends on to {export_slice}.py",
)
@click.option(
    "--export-slice-to-airflow-dag",
    "--airflow",
    default=None,
    help="Requires --slice. Export the sliced code from all slices to an Airflow DAG {export-slice-to-airflow-dag}.py",
)
@click.option(
    "--airflow-task-dependencies",
    default=None,
    help="Optional flag for --airflow. Specifies tasks dependencies in Airflow format, i.e. 'p value' >> 'y' or 'p value', 'x' >> 'y'. Put slice names under single quotes.",
)
@click.option(
    "--print-source", help="Whether to print the source code", is_flag=True
)
@click.option(
    "--print-graph",
    help="Whether to print the generated graph code",
    is_flag=True,
)
@click.option(
    "--verbose",
    help="Print out logging for graph creation and execution",
    is_flag=True,
)
@click.option(
    "--visualize",
    help="Visualize the resulting graph with Graphviz",
    is_flag=True,
)
@click.argument(
    "file_name",
    type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path),
)
def python(
    file_name: pathlib.Path,
    db_url: str,
    slice: List[str],  # cast tuple into list
    export_slice: List[str],  # cast tuple into list
    export_slice_to_airflow_dag: str,
    airflow_task_dependencies: str,
    print_source: bool,
    print_graph: bool,
    verbose: bool,
    visualize: bool,
):
    set_custom_excepthook()
    configure_logging("INFO" if verbose else "WARNING")
    tree = rich.tree.Tree(f"📄 {file_name}")

    db = RelationalLineaDB.from_environment(db_url)
    code = file_name.read_text()

    if print_source:
        tree.add(
            rich.console.Group(
                "Source code", rich.syntax.Syntax(code, "python")
            )
        )

    # Change the working directory to that of the script,
    # To pick up relative data paths
    os.chdir(file_name.parent)

    tracer = Tracer(db, SessionType.SCRIPT)
    transform(code, file_name, tracer)

    if visualize:
        from lineapy.visualizer import Visualizer

        Visualizer.for_public(tracer).render_pdf_file()

    if slice and not export_slice and not export_slice_to_airflow_dag:
        for _slice in slice:
            tree.add(
                rich.console.Group(
                    f"Slice of {repr(_slice)}",
                    rich.syntax.Syntax(tracer.slice(_slice), "python"),
                )
            )

    if export_slice:
        if not slice:
            print("Please specify --slice. It is required for --export-slice")
            exit(1)
        for _slice, _export_slice in zip(slice, export_slice):
            full_code = tracer.slice(_slice)
            pathlib.Path(f"{_export_slice}.py").write_text(full_code)

    if export_slice_to_airflow_dag:
        if not slice:
            print(
                "Please specify --slice. It is required for --export-slice-to-airflow-dag"
            )
            exit(1)

        full_code = sliced_airflow_dag(
            tracer,
            slice,
            export_slice_to_airflow_dag,
            airflow_task_dependencies,
        )
        pathlib.Path(f"{export_slice_to_airflow_dag}.py").write_text(full_code)

    tracer.db.close()
    if print_graph:
        graph_code = prettify(
            tracer.graph.print(
                include_source_location=False,
                include_id_field=False,
                include_session=False,
                include_imports=False,
            )
        )
        tree.add(
            rich.console.Group(
                "፨ Graph", rich.syntax.Syntax(graph_code, "python")
            )
        )

    console = rich.console.Console()
    console.print(tree)


@linea_cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("jupyter_args", nargs=-1, type=click.UNPROCESSED)
def jupyter(jupyter_args):
    run_with_ipython_dir("jupyter", *jupyter_args)


@linea_cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("ipython_args", nargs=-1, type=click.UNPROCESSED)
def ipython(ipython_args):
    run_with_ipython_dir("ipython", *ipython_args)


def run_with_ipython_dir(*args: str) -> None:
    """
    Runs the command with a custom ipython directory set
    so that the lineapy extension is loaded by default.
    """
    with tempfile.TemporaryDirectory() as ipython_dir_name:
        # Make a default profile with the extension added to the ipython and kernel
        # configs
        profile_dir = pathlib.Path(ipython_dir_name) / "profile_default"
        profile_dir.mkdir()
        settings = 'c.InteractiveShellApp.extensions = ["lineapy"]'
        (profile_dir / "ipython_config.py").write_text(settings)
        (profile_dir / "ipython_kernel_config.py").write_text(settings)

        env = copy(os.environ)
        env["IPYTHONDIR"] = ipython_dir_name

        subprocess.run(args, env=env)


if __name__ == "__main__":
    linea_cli()
