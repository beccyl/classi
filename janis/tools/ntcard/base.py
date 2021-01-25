from janis_bioinformatics.tools import BioinformaticsTool
from datetime import datetime

from janis_core import (
    ToolOutput,
    ToolInput,
    Boolean,
    String,
    Int,
    File,
    Array,
    ToolMetadata,
    WildcardSelector,
)

from janis_bioinformatics.data_types import Fastq, Fasta, FastqGz, FastaGz, Sam, Bam
from janis_core.types.common_data_types import UnionType

class NtCardToolBase(BioinformaticsTool):
    def tool_provider(self):
        return "ntcard"

    def tool(self):
        return "ntcard"

    def base_command(self):
        return ["ntcard"]

    def inputs(self):
        return [
            ToolInput(
                "files",
                Array(UnionType(Fastq, Fasta, Sam, Bam, FastqGz, FastaGz)),
                position=10,
                localise_file=True,
                doc="Acceptable file formats: fastq, fasta, sam, bam and in compressed formats gz, bz, zip, xz. ",
            ),
            ### not implemented @ prefix
            ### A list of files containing file names in each row can be passed with @ prefix.
            ToolInput(
                "cov",
                Int(optional=True),
                prefix=("-c"),
                doc="(--cov=N)  the maximum coverage of kmer in output [1000]",
            ),
            ToolInput(
                "gap",
                Int(optional=True),
                prefix=("-g"),
                doc="(--gap=N)  the length of gap in the gap seed [0]. g mod 2 must equal k mod 2 unless g == 0. "
                    "-g does not support multiple k currently.",
            ),
            ToolInput(
                "kmer",
                Int(),
                prefix=("-k"),
                doc="(--kmer=N)  the length of kmer. Required.",
            ),
            ToolInput(
                "threads",
                Int(optional=True),
                prefix=("-t"),
                doc="(--threads=N)  use N parallel threads [1] (N>=2 should be used when input files are >=2)",
            ),
            ToolInput(
                "prefix",
                String(optional=True),
                prefix=("-p"),
                doc="(--prefix=STRING)  the prefix for output file name(s)",
            ),
            ToolInput(
                "outputFilename",
                String(optional=True),
                prefix=("-o"),
                doc="(--output=STRING)  the name for output file name (used when output should be a single file)",
            ),
            ToolInput(
                "help",
                Boolean(optional=True),
                prefix=("--help"),
                doc="(--help)  display this help and exit",
            ),
            ToolInput(
                "version",
                Boolean(optional=True),
                prefix=("--version"),
                doc="(--version)  output version information and exit",
            ),
        ]
    def outputs(self):
        return [
            ToolOutput(
                "out",
                File,
                glob=WildcardSelector("*.hist")
            )
        ]

    def doc(self):
        return (
            "ntCard is a streaming algorithm for cardinality estimation in genomics datasets. As input it "
            "takes file(s) in fasta, fastq, sam, or bam formats and computes the total number of distinct "
            "k-mers, F0, and also the k-mer coverage frequency histogram, fi, i>=1. "
            "Documentation: ihttps://github.com/bcgsc/ntCard#ntcard"
        )

    def arguments(self):
        return []

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Rebecca Evans (beccyl)"],
            dateCreated=datetime(2021, 1, 25),
            dateUpdated=datetime(2021, 1, 25),
            institution=None,
            doi="doi:10.1093/bioinformatics/btw832",
            citation="Hamid Mohamadi, Hamza Khan, and Inanc Birol. ntCard: a streaming algorithm for "
                "cardinality estimation in genomics data. "
                "Bioinformatics (2017) 33 (9): 1324-1330. 10.1093/bioinformatics/btw832",
            keywords=["ntcard"],
            documentationUrl="https://www.bcgsc.ca/resources/software/ntcard",
            documentation="ntCard is a streaming algorithm for estimating the frequencies of k-mers "
                "in genomics datasets. At its core, ntCard uses the ntHash algorithm to efficiently "
                "compute hash values for streamed sequences. It then samples the calculated hash "
                "values to build a reduced representation multiplicity table describing the sample "
                "distribution. Finally, it uses a statistical model to reconstruct the population "
                "distribution from the sample distribution."
        )

