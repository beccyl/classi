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

class SqueakrCountBase(SqueakrToolBase, ABC):
    @classmethod
    def squeakr_command(cls):
        return "count"

    def friendly_name(self) -> str:
        return "Squeakr: Count"

    def tool(self) -> str:
        return "SqueakrCount"

    def inputs(self):
        return [
            ToolInput(
                tag="exact",
                input_type=Boolean(optional=True),
                prefix="--exact",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-e)  squeakr-exact (default is Squeakr approximate). Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="kmer_size",
                input_type=Int,
                prefix="-k",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-k)  <k-size> length of k-mers to count. Required."
                ),
            ),
            ToolInput(
                tag="cutoff",
                input_type=Int(optional=True),
                prefix="-c",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-c)  <cutoff> only output k-mers with count greater than or equal to cutoff (default = 1).  Optional."
                ),
            ),
            ToolInput(
                tag="no_counts",
                input_type=Boolean(optional=True),
                prefix="--no-counts",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-n)  only output k-mers and no counts (default = false). Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="log_slots",
                input_type=Int(optional=True),
                prefix="-s",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-s)  <log-slots> log of number of slots in the CQF. (Size argument is only optional when numthreads is exactly 1.)"
                ),
            ),
            ToolInput(
                tag="num_threads",
                input_type=Int(optional=True),
                prefix="-t",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-t)  number of threads to use to count (default = number of hardware threads)."
                ),
            ),
            ToolInput(
                tag="input_list",
                input_type=Array(UnionType(Fastq, FastqGz)),
                position=10,
                doc=InputDocumentation(
                    doc="(-i)  file containing list of input filters. Required."
                ),
            ),
            ToolInput(
                tag="out_file",
                input_type=Filename(
                    prefix="./output",  ## squeakr bug(?) needs directory name
                    extension=".squeakr",
                    optional=False,
                ),
                prefix="-o",
                position=9,
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
                glob=InputSelector("out_file"),
            )
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Rebecca Evans (beccyl)"],
            dateCreated=datetime(2021, 1, 25),
            dateUpdated=datetime(2021, 1, 25),
            institution="Splatlab",
            doi="10.1093/bioinformatics/btx636",
            keywords=["splatlab", "squeakr", "count"],
            citation="Prashant Pandey, Michael A Bender, Rob Johnson, Rob Patro, "
            "Squeakr: an exact and approximate k-mer counting system, "
            "Bioinformatics, Volume 34, Issue 4, 15 February 2018, Pages 568–575,",
            documentation="""
SYNOPSIS
        squeakr count [-e] -k <k-size> [-c <cutoff>] [-n] [-s <log-slots>] [-t <num-threads>] -o <out-file> <files>...

OPTIONS
        -e, --exact squeakr-exact (default is Squeakr approximate)
        <k-size>    length of k-mers to count
        <cutoff>    only output k-mers with count greater than or equal to cutoff (default = 1)

        -n, --no-counts
                    only output k-mers and no counts (default = false)

        <log-slots> log of number of slots in the CQF. (Size argument is only optional when numthreads is exactly 1.)

        <num-threads>
                    number of threads to use to count (default = number of hardware threads)

        <out-file>  file in which output should be written
        <files>...  list of files to be counted (supported files: fastq and compressed gzip or bzip2 fastq files)
""",
        )
