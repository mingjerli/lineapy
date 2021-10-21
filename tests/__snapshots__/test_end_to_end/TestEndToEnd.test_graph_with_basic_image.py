import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy
import pandas as pd
import matplotlib.pyplot as plt
from PIL.Image import open

df = pd.read_csv(\'tests/simple_data.csv\')
plt.imsave(\'simple_data.png\', df)

img = open(\'simple_data.png\')
img = img.resize([200, 200])

lineapy.linea_publish(img, "Graph With Image")
""",
    location=PosixPath("[source file path]"),
)
call_5 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=33,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=10,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            ImportNode(
                source_location=SourceLocation(
                    lineno=3,
                    col_offset=0,
                    end_lineno=3,
                    end_col_offset=31,
                    source_code=source_1.id,
                ),
                library=Library(
                    name="matplotlib.pyplot",
                ),
            ).id,
            LiteralNode(
                value="imsave",
            ).id,
        ],
        global_reads={},
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=11,
                end_lineno=7,
                end_col_offset=28,
                source_code=source_1.id,
            ),
            value="simple_data.png",
        ).id,
        CallNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=5,
                end_lineno=6,
                end_col_offset=41,
                source_code=source_1.id,
            ),
            function_id=CallNode(
                source_location=SourceLocation(
                    lineno=6,
                    col_offset=5,
                    end_lineno=6,
                    end_col_offset=16,
                    source_code=source_1.id,
                ),
                function_id=LookupNode(
                    name="getattr",
                ).id,
                positional_args=[
                    ImportNode(
                        source_location=SourceLocation(
                            lineno=2,
                            col_offset=0,
                            end_lineno=2,
                            end_col_offset=19,
                            source_code=source_1.id,
                        ),
                        library=Library(
                            name="pandas",
                        ),
                    ).id,
                    LiteralNode(
                        value="read_csv",
                    ).id,
                ],
                global_reads={},
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=17,
                        end_lineno=6,
                        end_col_offset=40,
                        source_code=source_1.id,
                    ),
                    value="tests/simple_data.csv",
                ).id
            ],
            global_reads={},
        ).id,
    ],
    global_reads={},
)
call_9 = CallNode(
    source_location=SourceLocation(
        lineno=10,
        col_offset=6,
        end_lineno=10,
        end_col_offset=28,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=10,
            col_offset=6,
            end_lineno=10,
            end_col_offset=16,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            CallNode(
                source_location=SourceLocation(
                    lineno=9,
                    col_offset=6,
                    end_lineno=9,
                    end_col_offset=29,
                    source_code=source_1.id,
                ),
                function_id=CallNode(
                    function_id=LookupNode(
                        name="getattr",
                    ).id,
                    positional_args=[
                        ImportNode(
                            source_location=SourceLocation(
                                lineno=4,
                                col_offset=0,
                                end_lineno=4,
                                end_col_offset=26,
                                source_code=source_1.id,
                            ),
                            library=Library(
                                name="PIL.Image",
                            ),
                        ).id,
                        LiteralNode(
                            value="open",
                        ).id,
                    ],
                    global_reads={},
                ).id,
                positional_args=[
                    LiteralNode(
                        source_location=SourceLocation(
                            lineno=9,
                            col_offset=11,
                            end_lineno=9,
                            end_col_offset=28,
                            source_code=source_1.id,
                        ),
                        value="simple_data.png",
                    ).id
                ],
                global_reads={},
            ).id,
            LiteralNode(
                value="resize",
            ).id,
        ],
        global_reads={},
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=10,
                col_offset=17,
                end_lineno=10,
                end_col_offset=27,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="__build_list__",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=10,
                        col_offset=18,
                        end_lineno=10,
                        end_col_offset=21,
                        source_code=source_1.id,
                    ),
                    value=200,
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=10,
                        col_offset=23,
                        end_lineno=10,
                        end_col_offset=26,
                        source_code=source_1.id,
                    ),
                    value=200,
                ).id,
            ],
            global_reads={},
        ).id
    ],
    global_reads={},
)
