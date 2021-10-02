import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="ls=[1,2,3]\na=1\nls[1:a]",
    working_directory="dummy_linea_repo/",
    libraries=[],
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=7,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=VariableNode(
                id=get_new_id(),
                session_id=session.id,
                source_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=1,
                    col_offset=0,
                    end_lineno=1,
                    end_col_offset=10,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=1,
                                col_offset=4,
                                end_lineno=1,
                                end_col_offset=5,
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
                                col_offset=6,
                                end_lineno=1,
                                end_col_offset=7,
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
                                col_offset=8,
                                end_lineno=1,
                                end_col_offset=9,
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
                assigned_variable_name="ls",
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=CallNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=3,
                col_offset=3,
                end_lineno=3,
                end_col_offset=6,
                arguments=[
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=0,
                        value_node_id=LiteralNode(
                            id=get_new_id(),
                            session_id=session.id,
                            lineno=3,
                            col_offset=3,
                            end_lineno=3,
                            end_col_offset=4,
                            value=1,
                        ).id,
                    ).id,
                    ArgumentNode(
                        id=get_new_id(),
                        session_id=session.id,
                        positional_order=1,
                        value_node_id=VariableNode(
                            id=get_new_id(),
                            session_id=session.id,
                            source_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=2,
                                col_offset=0,
                                end_lineno=2,
                                end_col_offset=3,
                                value=1,
                            ).id,
                            assigned_variable_name="a",
                        ).id,
                    ).id,
                ],
                function_id=LookupNode(
                    id=get_new_id(),
                    session_id=session.id,
                    name="slice",
                ).id,
            ).id,
        ).id,
    ],
    function_id=LookupNode(
        id=get_new_id(),
        session_id=session.id,
        name="getitem",
    ).id,
)
