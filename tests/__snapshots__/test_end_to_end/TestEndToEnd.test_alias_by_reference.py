import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="a = [1,2,3]\nb = a\na.append(4)\ns = sum(b)\n",
    working_directory="dummy_linea_repo/",
    libraries=[],
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=5,
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=11,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=5,
                    end_lineno=1,
                    end_col_offset=6,
                    value=1,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=7,
                    end_lineno=1,
                    end_col_offset=8,
                    value=2,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=2,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=9,
                    end_lineno=1,
                    end_col_offset=10,
                    value=3,
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="__build_list__",
        ).id,
    ).id,
    assigned_variable_name="a",
)
call_4 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=11,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=3,
                col_offset=9,
                end_lineno=3,
                end_col_offset=10,
                value=4,
            ).id,
        ).id
    ],
    function_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=8,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=variable_1.id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    value="append",
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="getattr",
        ).id,
    ).id,
)
variable_3 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=4,
        col_offset=0,
        end_lineno=4,
        end_col_offset=10,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=VariableNode(
                    id=get_new_id(),
                    session_id=session.id,
                    source_node_id=variable_1.id,
                    assigned_variable_name="b",
                ).id,
            ).id
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="sum",
        ).id,
    ).id,
    assigned_variable_name="s",
)