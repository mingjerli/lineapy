import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy
a = 10
fn = lambda x: a + x
r = sum(map(fn, [1]))

lineapy.linea_publish(r, \'r\')
""",
    location=PosixPath("[source file path]"),
)
literal_4 = LiteralNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=4,
        end_lineno=2,
        end_col_offset=6,
        source_code=source_1.id,
    ),
    value=10,
)
call_5 = CallNode(
    source_location=SourceLocation(
        lineno=4,
        col_offset=4,
        end_lineno=4,
        end_col_offset=21,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="sum",
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=4,
                col_offset=8,
                end_lineno=4,
                end_col_offset=20,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="map",
            ).id,
            positional_args=[
                CallNode(
                    function_id=LookupNode(
                        name="getitem",
                    ).id,
                    positional_args=[
                        CallNode(
                            source_location=SourceLocation(
                                lineno=3,
                                col_offset=5,
                                end_lineno=3,
                                end_col_offset=20,
                                source_code=source_1.id,
                            ),
                            function_id=LookupNode(
                                name="__exec__",
                            ).id,
                            positional_args=[
                                LiteralNode(
                                    value="lambda x: a + x",
                                ).id,
                                LiteralNode(
                                    value=True,
                                ).id,
                            ],
                        ).id,
                        LiteralNode(
                            value=0,
                        ).id,
                    ],
                ).id,
                CallNode(
                    source_location=SourceLocation(
                        lineno=4,
                        col_offset=16,
                        end_lineno=4,
                        end_col_offset=19,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="__build_list__",
                    ).id,
                    positional_args=[
                        LiteralNode(
                            source_location=SourceLocation(
                                lineno=4,
                                col_offset=17,
                                end_lineno=4,
                                end_col_offset=18,
                                source_code=source_1.id,
                            ),
                            value=1,
                        ).id
                    ],
                ).id,
            ],
        ).id
    ],
)
