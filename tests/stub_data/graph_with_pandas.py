from datetime import datetime

from lineapy.data.graph import Graph
from lineapy.data.types import (
    ImportNode,
    Library,
    ArgumentNode,
    CallNode,
    SessionContext,
    SessionType,
)
from tests.util import get_new_id

"""
The simple graph represents the execution of the following:

```
import pandas as pd
df = pd.read_csv('test_data.csv')
```

Notes:
- we don't really need NodeContext for execution so we are skipping it for now
- the UUIDs are kept constant so we can more easily reference the same values in a different file
"""

session = SessionContext(
    uuid=get_new_id(),
    file_name="testing.py",
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.now(),
)

line_1_id = get_new_id()

line_1 = ImportNode(
    id=line_1_id,
    session_id=session.uuid,
    code="import pandas as pd",
    library=Library(name="pandas", version="1", path=""),
    alias="pd",
)

arg_literal_id = get_new_id()

arg_file = "./tests/ames_train_cleaned.csv"
arg_literal = ArgumentNode(
    id=arg_literal_id,
    session_id=session.uuid,
    positional_order=1,
    value_literal=arg_file,
)

line_2_id = get_new_id()

line_2 = CallNode(
    id=line_2_id,
    session_id=session.uuid,
    code="pd.read_csv('%s')" % arg_file,
    function_name="read_csv",
    function_module=line_1_id,
    assigned_variable_name="df",
    arguments=[arg_literal],
)

graph_with_pandas = Graph([line_1, line_2, arg_literal])
