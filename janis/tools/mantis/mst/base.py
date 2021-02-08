from abc import ABC
from datetime import datetime

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    InputSelector,
    Filename,
    Directory,
    ToolMetadata,
    InputDocumentation,
)

from ..mantistoolbase import MantisToolBase

class MantisMstBase(MantisToolBase, ABC):
    @classmethod
    def mantis_command(cls):
        return "mst"

    def friendly_name(self) -> str:
        return "Mantis: Mst"

    def tool(self) -> str:
        return "MantisMst"

    def inputs(self):
        return [
            ToolInput(
                tag="delete_RRR",
                input_type=Boolean(optional=True),
                prefix="--delete-RRR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-d)  Remove the previous color class RRR representation."
                ),
            ),
            ToolInput(
                tag="keep_RRR",
                input_type=Boolean(optional=True),
                prefix="--keep-RRR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-k)  Keep the previous color class RRR representation."
                ),
            ),
            ToolInput(
                tag="threads",
                input_type=Int(optional=True),
                prefix="-t",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-t)  number of threads."
                ),
            ),
            ToolInput(
                tag="index_prefix",
                input_type=Filename(),
                prefix="-p",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-p)  The directory where the index is stored. Required."
                ),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Directory(),
                selector=InputSelector("index_prefix"),
            )
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Rebecca Evans (beccyl)"],
            dateCreated=datetime(2021, 2, 2),
            dateUpdated=datetime(2021, 2, 2),
            institution="Splatlab",
            doi=None,
            keywords=["splatlab", "mantis", "mst"],
            citation="""Prashant Pandey, Fatemeh Almodaresi, Michael A. Bender, Michael Ferdman, Rob Johnson, and Rob Patro. "Mantis: A Fast, Small, and Exact Large-Scale Sequence-Search Index." Cell Systems (2018). Fatemeh Almodaresi, Prashant Pandey, Michael Ferdman, Rob Johnson, and Rob Patro. "An Efficient, Scalable and Exact Representation of High-Dimensional Color Information Enabled via de Bruijn Graph Search." RECOMB (2019).""",
            documentation="""
SYNOPSIS
        mantis mst -p <index_prefix> [-t <num_threads>] (-k|-d)

OPTIONS
        <index_prefix>
                    The directory where the index is stored.

        <num_threads>
                    number of threads

        -k, --keep-RRR
                    Keep the previous color class RRR representation.

        -d, --delete-RRR
                    Remove the previous color class RRR representation.
""",
        )
