from abc import ABC
from datetime import datetime

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    Array,
    File,
    Boolean,
    String,
    Int,
    InputSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
)

from janis_bioinformatics.data_types import Fastq, FastqGz
from janis_core.types.common_data_types import UnionType

from ..squeakrtoolbase import SqueakrToolBase

class SqueakrQueryBase(SqueakrToolBase, ABC):
    @classmethod
    def squeakr_command(cls):
        return "query"

    def friendly_name(self) -> str:
        return "Squeakr: Query"

    def tool(self) -> str:
        return "SqueakrQuery"

    def inputs(self):
        return [
            ToolInput(
                tag="squeakr_file",
                input_type=File(optional=False),
                prefix="-f",
                position=1,
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-f)  input squeakr file. Required."
                ),
            ),
            ToolInput(
                tag="query_file",
                input_type=File(optional=False),
                prefix="-q",
                position=2,
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-q)  input query file. Required."
                ),
            ),
            ToolInput(
                tag="output_file",
                input_type=Filename(
                    prefix="./query",  ## squeakr bug(?) needs directory name
                    extension=".output",
                    optional=False,
                ),
                prefix="-o",
                position=3,
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-o)  file in which output should be written. Required."
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
            doi="10.1093/bioinformatics/btx636",
            keywords=["splatlab", "squeakr", "query"],
            citation="Prashant Pandey, Michael A Bender, Rob Johnson, Rob Patro, "
            "Squeakr: an exact and approximate k-mer querying system, "
            "Bioinformatics, Volume 34, Issue 4, 15 February 2018, Pages 568–575,",
            documentation="""
SYNOPSIS
        squeakr query -f <squeakr-file> -q <query-file> -o <output-file>

OPTIONS
        <squeakr-file>
                    input squeakr file

        <query-file>
                    input query file

        <output-file>
                    output file
""",
        )
