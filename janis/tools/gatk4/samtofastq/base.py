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
    WildcardSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
)

from janis_bioinformatics.data_types import BamBai, Bam, FastqGz
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase


class Gatk4SamToFastqBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "SamToFastq"

    def friendly_name(self) -> str:
        return "Gatk4: SamToFastq"

    def tool(self) -> str:
        return "GatkSamToFastq"

    def inputs(self):
        return [
            *super().inputs(),
            ToolInput(
                tag="inp",
                input_type=Bam(),
                prefix="--INPUT",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) Input file SAM/BAM to extract reads from. Required."
                ),
            ),
            ## default assume pairend end. TODO:
            ToolInput(
                tag="fastq",
                input_type=Filename(
                    prefix=InputSelector("inp", remove_file_extension=True),
                    suffix=".R1",
                    extension=".fastq.gz",
                    optional=False,
                ),
                prefix="--FASTQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F) Output FASTQ file (single-end fastq or, if paired first end of the pair FASTQ). Required."
                ),
            ),
            # Optional Tool Arguments
            ToolInput(
                tag="arguments_file",
                input_type=File(optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    "read one or more arguments files and add them to the command line"
                ),
            ),
            ToolInput(
                tag="clipping_action",
                input_type=String(optional=True),
                prefix="--CLIPPING_ACTION",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CLIP_ACT)  The action that should be taken with clipped reads: 'X' means the reads and qualities should be trimmed at the clipped position; 'N' means the bases should be changed to Ns in the clipped region; and any integer means that the base qualities should be set to that value in the clipped region."
                ),
            ),
            ToolInput(
                tag="clipping_attribute",
                input_type=String(optional=True),
                prefix="--CLIPPING_ATTRIBUTE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CLIP_ATTR)  The attribute that stores the position at which the SAM record should be clipped"
                ),
            ),
            ToolInput(
                tag="clipping_min_length",
                input_type=Int(optional=True),
                prefix="--CLIPPING_MIN_LENGTH",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CLIP_MIN)  When performing clipping with the CLIPPING_ATTRIBUTE and CLIPPING_ACTION parameters, ensure that the resulting reads after clipping are at least CLIPPING_MIN_LENGTH bases long. If the original read is shorter than CLIPPING_MIN_LENGTH then the original read length will be maintained.  Default value: 0."
                ),
            ),
            # TODO: defined in super ?
            #ToolInput(
            #    tag="compression_level",
            #    input_type=Int(optional=True),
            #    prefix="--COMPRESSION_LEVEL",
            #    separate_value_from_prefix=True,
            #    doc=InputDocumentation(
            #        doc="Compression level for all compressed files created (e.g. BAM and VCF). Default value: 2."
            #    ),
            #),
            ToolInput(
                tag="compress_outputs_per_rg",
                input_type=Boolean(optional=True),
                prefix="--COMPRESS_OUTPUTS_PER_RG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-GZOPRG)  Compress output FASTQ files per read group using gzip and append a .gz extension to the file names. Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="create_index",
                input_type=Boolean(optional=True),
                prefix="--CREATE_INDEX",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an index when writing VCF or coordinate sorted BAM output. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="create_md5_file",
                input_type=Boolean(optional=True),
                prefix="--CREATE_MD5_FILE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to create an MD5 digest for any BAM or FASTQ files created. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="ga4gh_client_secrets",
                input_type=File(optional=True),
                prefix="--GA4GH_CLIENT_SECRETS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Google Genomics API client_secrets.json file path.  Default value: client_secrets.json."),
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="include_non_pf_reads",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PF_READS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-NON_PF)  Include non-PF reads from the SAM file into the output FASTQ files. PF means 'passes filtering'. Reads whose 'not passing quality controls' flag is set are non-PF reads. See GATK Dictionary for more info. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="include_non_primary_alignments",
                input_type=Boolean(optional=True),
                prefix="--INCLUDE_NON_PRIMARY_ALIGNMENTS",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="If true, include non-primary alignments in the output. Support of non-primary alignments in SamToFastq is not comprehensive, so there may be exceptions if this is set to true and there are paired reads with non-primary alignments. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="interleave",
                input_type=Boolean(optional=True),
                prefix="--INTERLEAVE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-INTER) Will generate an interleaved fastq if paired, each line will have /1 or /2 to describe which end it came from. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="max_records_in_ram",
                input_type=Int(optional=True),
                prefix="--MAX_RECORDS_IN_RAM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="When writing files that need to be sorted, this will specify the number of records stored in RAM before spilling to disk. Increasing this number reduces the number of file handles needed to sort the file, and increases the amount of RAM needed.  Default value: 500000. "
                ),
            ),
            ### TODO: need to test this option
            ToolInput(
                tag="output_dir",
                input_type=File(optional=True),
                prefix="--OUTPUT_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Directory in which to output the FASTQ file(s). Used only when OUTPUT_PER_RG is true."
                ),
            ),
            ToolInput(
                tag="output_per_rg",
                input_type=Boolean(optional=True),
                prefix="--OUTPUT_PER_RG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OPRG) Output a FASTQ file per read group (two FASTQ files per read group if the group is paired). Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="quality",
                input_type=Int(optional=True),
                prefix="--QUALITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-Q)  End-trim reads using the phred/bwa quality trimming algorithm and this quality."
                ),
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="re_reverse",
                input_type=Boolean(optional=True),
                prefix="--RE_REVERSE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RC)  Re-reverse bases and qualities of reads with negative strand flag set before writing them to FASTQ.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="read1_max_bases_to_write",
                input_type=Int(optional=True),
                prefix="--READ1_MAX_BASES_TO_WRITE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R1_MAX_BASES)  The maximum number of bases to write from read 1 after trimming. If there are fewer than this many bases left after trimming, all will be written. If this value is null then all bases left after trimming will be written."
                ),
            ),
            ToolInput(
                tag="read1_trim",
                input_type=Int(optional=True),
                prefix="--READ1_TRIM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R1_TRIM)  The number of bases to trim from the beginning of read 1.  Default value: 0."
                ),
            ),
            ToolInput(
                tag="read2_max_bases_to_write",
                input_type=Int(optional=True),
                prefix="--READ2_MAX_BASES_TO_WRITE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R2_MAX_BASES)  The maximum number of bases to write from read 2 after trimming. If there are fewer than this many bases left after trimming, all will be written. If this value is null then all bases left after trimming will be written."
                ),
            ),
            ToolInput(
                tag="read2_trim",
                input_type=Int(optional=True),
                prefix="--READ2_TRIM",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-R2_TRIM)  The number of bases to trim from the beginning of read 2.  Default value: 0."
                ),
            ),
            ToolInput(
                tag="reference_sequence",
                input_type=File(optional=True),
                prefix="--REFERENCE_SEQUENCE",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    "(-R)  Reference sequence file"
                ),
            ),
            ToolInput(
                tag="rg_tag",
                input_type=String(optional=True),
                prefix="--RG_TAG",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    "(-RGT)  The read group tag (PU or ID) to be used to output a FASTQ file per read group. Default value: PU"
                ),
            ),
            ToolInput(
                tag="second_end_fastq",
                input_type=Filename(
                    prefix=InputSelector("inp", remove_file_extension=True),
                    suffix=".R2",
                    extension=".fastq.gz",
                    optional=True,
                ),
                prefix="--SECOND_END_FASTQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-F2)  Output FASTQ file (if paired, second end of the pair FASTQ)."
                ),
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tmp_dir",
                input_type=File(optional=True),
                prefix="--TMP_DIR",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more directories with space available to be used by this program for temporary storage of working files.  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="unpaired_fastq",
                input_type=Filename(
                    prefix=InputSelector("inp", remove_file_extension=True),
                    suffix=".U",
                    extension=".fastq.gz",
                    optional=True,
                ),
                prefix="--UNPAIRED_FASTQ",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-FU)  Output FASTQ file for unpaired reads; may only be provided in paired-FASTQ mode."
                ),
            ),
            ToolInput(
                tag="use_jdk_deflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_DEFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_deflater)  Use the JDK Deflater instead of the Intel Deflater for writing compressed output.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="use_jdk_inflater",
                input_type=Boolean(optional=True),
                prefix="--USE_JDK_INFLATER",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-use_jdk_inflater)  Use the JDK Inflater instead of the Intel Inflater for reading compressed input.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="validation_stringency",
                input_type=String(optional=True),
                prefix="--VALIDATION_STRINGENCY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Validation stringency for all SAM files read by this program.  Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: STRICT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--VERBOSITY",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Control verbosity of logging. Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
                ),
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="display the version number for this tool. Default value: false. Possible values: {true, false} "
                ),
            ),
        ]

    def outputs(self):
        return [
            #ToolOutput(
            #    "out",
            #    Fastq(),
            #    glob=InputSelector("fastq"),
            #    doc="Fastq to write extracted reads to",
            #),
            ToolOutput(
                "out",
                Array(FastqGz),
                glob=WildcardSelector("*.fastq.gz"),
                doc="Fastq gzipped output file(s).  May contain single-end or paired-end, or interleaved paired-end.",
            ),
        ]

    def bind_metadata(self):
        return ToolMetadata(
            contributors=["Rebecca Evans (@beccyl)"],
            dateCreated=datetime(2021, 1, 18),
            dateUpdated=datetime(2021, 1, 18),
            institution="Broad Institute",
            doi=None,
            citation="See https://software.broadinstitute.org/gatk/documentation/article?id=11027 for more information",
            keywords=["gatk", "gatk4", "broad", "picard", "sam", "fastq"],
            documentationUrl="https://gatk.broadinstitute.org/hc/en-us/articles/360037594271-SamToFastq-Picard-",
            documentation="""
USAGE: SamToFastq [arguments]

Converts a SAM or BAM file to FASTQ. Extracts read sequences and qualities from the input SAM/BAM file and writes them intothe output file in Sanger FASTQ format. See MAQ FASTQ specification for details. This tool can be used by way of a pipe to run BWA MEM on unmapped BAM (uBAM) files efficiently.

In the RC mode (default is True), if the read is aligned and the alignment is to the reverse strand on the genome, the read sequence from input sam file will be reverse-complemented prior to writing it to FASTQ in order restore correctlythe original read sequence as it was generated by the sequencer.

Example:

.. code-tool: none

   java -jar picard.jar SamToFastq \\
       I=input.bam \\
       FASTQ=output.fastq \\
""",
        )
