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

class MantisBuildBase(MantisToolBase, ABC):
    @classmethod
    def mantis_command(cls):
        return "build"

    def friendly_name(self) -> str:
        return "Mantis: Build"

    def tool(self) -> str:
        return "MantisBuild"

    def inputs(self):
        return [
            ToolInput(
                tag="eqclass_dist",
                input_type=Boolean(optional=True),
                prefix="--eqclass_dist",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-e)  write the eqclass abundance distribution. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="log_slots",
                input_type=Int,
                prefix="-s",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-s)  log of number of slots in the output CQF."
                ),
            ),
            ToolInput(
                tag="input_list",
                input_type=Filename(),
                prefix="-i",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-i)  file containing list of input filters. Required."
                ),
            ),
            ToolInput(
                tag="build_output",
                input_type=Filename(),
                prefix="-o",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-o)  directory where results should be written. Required."
                ),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                Directory(),
                glob=InputSelector("build_output"),
            )
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Rebecca Evans (beccyl)"],
            dateCreated=datetime(2021, 1, 19),
            dateUpdated=datetime(2021, 1, 19),
            institution="Splatlab",
            doi=None,
            keywords=["splatlab", "mantis", "build"],
            citation="""Prashant Pandey, Fatemeh Almodaresi, Michael A. Bender, Michael Ferdman, Rob Johnson, and Rob Patro. "Mantis: A Fast, Small, and Exact Large-Scale Sequence-Search Index." Cell Systems (2018). Fatemeh Almodaresi, Prashant Pandey, Michael Ferdman, Rob Johnson, and Rob Patro. "An Efficient, Scalable and Exact Representation of High-Dimensional Color Information Enabled via de Bruijn Graph Search." RECOMB (2019).""",
            documentation="""
SYNOPSIS
        mantis build [-e] -s <log-slots> -i <input_list> -o <build_output>

OPTIONS
        -e, --eqclass_dist
                    write the eqclass abundance distribution

        <log-slots> log of number of slots in the output CQF

        <input_list>
                    file containing list of input filters

        <build_output>
                    directory where results should be written
""",
        )
