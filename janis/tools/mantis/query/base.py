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

class MantisQueryBase(MantisToolBase, ABC):
    @classmethod
    def mantis_command(cls):
        return "query"

    def friendly_name(self) -> str:
        return "Mantis: Query"

    def tool(self) -> str:
        return "MantisQuery"

    def inputs(self):
        return [
            ToolInput(
                tag="use_colorclasses",
                input_type=Boolean(optional=True),
                prefix="--use-colorclasses",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-1)  Use color classes as the color info representation instead of MST."
                ),
            ),
            ToolInput(
                tag="json_output",
                input_type=Boolean(optional=True),
                prefix="--json",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-j)  Write the output in JSON format."
                ),
            ),
            ToolInput(
                tag="kmer",
                input_type=Int(optional=True),
                prefix="-k",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-k)  size of k for kmer."
                ),
            ),
            ToolInput(
                tag="query_prefix",
                input_type=Directory(optional=False),
                prefix="-p",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-p)  Prefix of input files. Required."
                ),
            ),
            ToolInput(
                tag="output_file",
                input_type=Filename(),
                prefix="-o",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-o)  Where to write query output."
                ),
            ),
            ToolInput(
                tag="query",
                input_type=File(optional=False),
                position=10,
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Query file. Required."
                ),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                File(),
                selector=InputSelector("output_file"),
            )
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Rebecca Evans (beccyl)"],
            dateCreated=datetime(2021, 2, 2),
            dateUpdated=datetime(2021, 2, 2),
            institution="Splatlab",
            doi=None,
            keywords=["splatlab", "mantis", "query"],
            citation="""Prashant Pandey, Fatemeh Almodaresi, Michael A. Bender, Michael Ferdman, Rob Johnson, and Rob Patro. "Mantis: A Fast, Small, and Exact Large-Scale Sequence-Search Index." Cell Systems (2018). Fatemeh Almodaresi, Prashant Pandey, Michael Ferdman, Rob Johnson, and Rob Patro. "An Efficient, Scalable and Exact Representation of High-Dimensional Color Information Enabled via de Bruijn Graph Search." RECOMB (2019).""",
            documentation="""
SYNOPSIS
        mantis query [-1] [-j] [-k <kmer>] -p <query_prefix> [-o <output_file>] <query>

OPTIONS
        -1, --use-colorclasses
                    Use color classes as the color info representation instead of MST

        -j, --json  Write the output in JSON format
        <kmer>      size of k for kmer.

        <query_prefix>
                    Prefix of input files.

        <output_file>
                    Where to write query output.

        <query>     Prefix of input files.
""",
        )
