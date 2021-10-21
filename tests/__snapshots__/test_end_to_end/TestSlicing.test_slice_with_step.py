import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="x = [1, 2, 3][::2]",
    location=PosixPath("[source file path]"),
)
call_3 = CallNode(
    source_location=SourceLocation(
        lineno=1,
        col_offset=4,
        end_lineno=1,
        end_col_offset=18,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="getitem",
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=4,
                end_lineno=1,
                end_col_offset=13,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="__build_list__",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=1,
                        col_offset=5,
                        end_lineno=1,
                        end_col_offset=6,
                        source_code=source_1.id,
                    ),
                    value=1,
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=1,
                        col_offset=8,
                        end_lineno=1,
                        end_col_offset=9,
                        source_code=source_1.id,
                    ),
                    value=2,
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=1,
                        col_offset=11,
                        end_lineno=1,
                        end_col_offset=12,
                        source_code=source_1.id,
                    ),
                    value=3,
                ).id,
            ],
            global_reads={},
        ).id,
        CallNode(
            source_location=SourceLocation(
                lineno=1,
                col_offset=14,
                end_lineno=1,
                end_col_offset=17,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="slice",
            ).id,
            positional_args=[
                LiteralNode().id,
                LiteralNode().id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=1,
                        col_offset=16,
                        end_lineno=1,
                        end_col_offset=17,
                        source_code=source_1.id,
                    ),
                    value=2,
                ).id,
            ],
            global_reads={},
        ).id,
    ],
    global_reads={},
)
