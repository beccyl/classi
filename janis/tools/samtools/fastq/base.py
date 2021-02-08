import os
import operator
from abc import ABC

from janis_core import (
    ToolInput,
    Filename,
    Int,
    String,
    Boolean,
    ToolOutput,
    Array,
    InputSelector,
    WildcardSelector,
    Stdout,
)
from janis_unix import TextFile
from janis_bioinformatics.data_types.bam import Bam
from janis_bioinformatics.data_types.fastq import Fastq
from janis_bioinformatics.tools.samtools.samtoolstoolbase import SamToolsToolBase
from janis_bioinformatics.tools.bioinformaticstoolbase import BioinformaticsTool
from janis_core import ToolMetadata


class SamToolsFastqBase(SamToolsToolBase, ABC):
    def tool(self):
        return "SamToolsFastq"

    @classmethod
    def samtools_command(cls):
        return "fastq"

    def inputs(self):
        return [
            *super(SamToolsFastqBase, self).inputs(),
            *SamToolsFastqBase.additional_inputs,
            ToolInput("bam", Bam(optional=False), position=10),
            ToolInput(
                "threads",
                Int(optional=True),
                position=5,
                prefix="-@",
                doc="Number of additional threads to use [0].",
            ),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Stdout(Fastq)),
            ToolOutput("nonspecific", Fastq(optional=True), selector=InputSelector("nonspecificFilename")),
            ToolOutput("read1", Fastq(optional=True), selector=InputSelector("read1Filename")),
            ToolOutput("read2", Fastq(optional=True), selector=InputSelector("read2Filename")),
            ToolOutput("singleton", Fastq(optional=True), selector=InputSelector("singletonFilename")),
            #ToolOutput("index1", Fastq(optional=True), selector=InputSelector("index1Filename")),
            #ToolOutput("index2", Fastq(optional=True), selector=InputSelector("index2Filename")),
        ]

    def friendly_name(self):
        return "SamTools: Fastq"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Rebecca Evans"],
            dateCreated=date(2021, 1, 5),
            dateUpdated=date(2021, 1, 5),
            institution="Samtools",
            doi=None,
            citation=None,  #find citation
            keywords=["samtools", "fastq"],
            documentationUrl="http://www.htslib.org/doc/samtools.html#COMMANDS_AND_OPTIONS",
            documentation="""Converts a BAM or CRAM into either FASTQ or FASTA format depending on the command invoked.
OPTIONS:

-n      By default, either '/1' or '/2' is added to the end of read names  where  the  corresponding
        BAM_READ1 or BAM_READ2 flag is set.  Using -n causes read names to be left as they are.

-N      Always add either '/1' or '/2' to the end of read names even when put into different files.

-O      Use quality values from OQ tags in preference to standard quality string if available.

-s FILE Write singleton reads in FASTQ format to FILE instead of outputting them.

-t      Copy RG, BC and QT tags to the FASTQ header line, if they exist.

-1 FILE Write reads with the BAM_READ1 flag set to FILE instead of outputting them.

-2 FILE Write reads with the BAM_READ2 flag set to FILE instead of outputting them.

-0 FILE Write reads with both or neither of the BAM_READ1 and BAM_READ2 flags set to FILE instead of
        outputting them.

-f INT  Only output alignments with all bits set in INT present in the FLAG field.  INT can be spec‐
        ified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with `0'
        (i.e. /^0[0-7]+/) [0].

-F INT  Do not output alignments with any bits set in INT present in the FLAG  field.   INT  can  be
        specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with
        `0' (i.e. /^0[0-7]+/) [0].

-G INT  Only EXCLUDE reads with all of the bits set in INT present in the FLAG field.   INT  can  be
        specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with
        `0' (i.e. /^0[0-7]+/) [0].

--i1 FILE
        write first index reads to FILE

--i2 FILE
        write second index reads to FILE

--barcode-tag TAG
        aux tag to find index reads in [default: BC]

--quality-tag TAG
        aux tag to find index quality in [default: QT]

--index-format STR
        string to describe how to parse the barcode and quality tags. For example:

        i14i8   the first 14 characters are index 1, the next 8 characters are index 2

        n8i14   ignore the first 8 characters, and use the next 14 characters for index 1

                If the tag contains a separator, then the numeric part can be replaced with  '*'  to
                mean 'read until the separator or end of tag', for example:

        n*i*    ignore the left part of the tag until the separator, then use the second part""",
        )
    additional_inputs = [
        ToolInput(
            "omitReadNumbers",
            Boolean(optional=True),
            prefix="-n",
            doc="Don't append /1 and /2 to the read name. "
            "By default, either '/1' or '/2' is added to the end of read names  where  the  corresponding "
            "BAM_READ1 or BAM_READ2 flag is set.  Using -n causes read names to be left as they are.",
        ),
        ToolInput(
            "appendReadNumbers",
            Boolean(optional=True),
            prefix="-N",
            doc="Always add either '/1' or '/2' to the end of read names even when put into different files.",
        ),
        ToolInput(
            "outputQuality",
            Boolean(optional=True),
            prefix="-O",
            doc="Use quality values from OQ tags in preference to standard quality string if available.",
        ),
        ToolInput(
            "copyTags",
            Boolean(optional=True),
            prefix="-t",
            doc="Copy RG, BC and QT tags to the FASTQ header line.",
        ),
        ToolInput(
            "requireAllFlagSet",
            Int(optional=True),
            prefix="-f",
            doc="Only output alignments with all bits set in INT present in the FLAG field.  INT can be "
            "specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with "
            "`0' (i.e. /^0[0-7]+/) [0].",
        ),
        ToolInput(
            "excludeAnyFlagSet",
            Int(optional=True),
            prefix="-F",
            doc="Do not output alignments with ANY bits set in INT present in the FLAG field.  INT can be "
            "specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with "
            "`0' (i.e. /^0[0-7]+/) [0].",
        ),
        ToolInput(
            "excludeAllFlagSet",
            Int(optional=True),
            prefix="-G",
            doc="Only EXCLUDE reads with ALL bits set in INT present in the FLAG field.  INT can be "
            "specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with "
            "`0' (i.e. /^0[0-7]+/) [0].",
        ),
        ToolInput(
            "nonspecificFilename",
            Filename(
                prefix=InputSelector("bam", remove_file_extension=True),
                suffix="_R0",
                extension=".fastq",
                optional=True,
            ),
            prefix="-0",
            default=None,
            doc="write paired reads flagged both or neither READ1 and READ2 to FILE",
        ),
        ToolInput(
            "read1Filename",
            Filename(
                prefix=InputSelector("bam", remove_file_extension=True),
                suffix="_R1",
                extension=".fastq",
                optional=True,
            ),
            prefix="-1",
            default=None,
            doc="write paired reads flagged READ1 to FILE",
        ),
        ToolInput(
            "read2Filename",
            Filename(
                prefix=InputSelector("bam", remove_file_extension=True),
                suffix="_R2",
                extension=".fastq",
                optional=True,
            ),
            prefix="-2",
            default=None,
            doc="write paired reads flagged READ2 to FILE",
        ),
        ToolInput(
            "singletonFilename",
            Filename(
                prefix=InputSelector("bam", remove_file_extension=True),
                suffix="_S",
                extension=".fastq",
                optional=True,
            ),
            prefix="-s",
            default=None,
            doc="write singleton reads to FILE [assume single-end]",
        ),
        #ToolInput(
        #    "index1Filename",
        #    Filename(
        #        prefix=InputSelector("bam", remove_file_extension=True),
        #        suffix="_I1",
        #        extension=".fastq",
        #        optional=True,
        #    ),
        #    prefix="--i1",
        #    doc="write first index reads to FILE",
        #),
        #ToolInput(
        #    "index2Filename",
        #    Filename(
        #        prefix=InputSelector("bam", remove_file_extension=True),
        #        suffix="_I2",
        #        extension=".fastq",
        #        optional=True,
        #    ),
        #    prefix="--i2",
        #    doc="write second index reads to FILE",
        #),
        ToolInput(
            "defaultQualityScore",
            Int(optional=True),
            prefix="-v",
            doc="default quality score if not given in file [1]",
        ),
        #ToolInput(
        #    "reference",
        #    String(optional=True),
        #    prefix="--reference",
        #    doc="Specifies a FASTA reference file for use in CRAM encoding or decoding. "
        #    "It usually is not required for decoding except in the situation of the MD5 not being obtainable "
        #    "via the REF_PATH or REF_CACHE environment variables.",
        #),
        #ToolInput(
        #    "inputFormatOptions",
        #    String(optional=True),
        #    prefix="--input-fmt-options",
        #    doc="OPT[=VAL] Specify a single input file format option in the form of OPTION or OPTION=VALUE",
        #),
        ToolInput(
            "barcodeTag",
            String(optional=True),
            prefix="--barcode-tag",
            doc="aux tag to find index reads in [default: BC]",
        ),
        ToolInput(
            "qualityTag",
            String(optional=True),
            prefix="--quality-tag",
            doc="aux tag to find index quality in [default: QT]",
        ),
        ToolInput(
            "indexFormat",
            String(optional=True),
            prefix="--index-format",
            doc="string to describe how to parse the barcode and quality tags. For example: "
                "i14i8   the first 14 characters are index 1, the next 8 characters are index 2.  "
                "n8i14   ignore the first 8 characters, and use the next 14 characters for index 1.  "
                "If the tag contains a separator, then the numeric part can be replaced with  '*'  to"
                "mean 'read until the separator or end of tag', for example: "
                "n*i*    ignore the left part of the tag until the separator, then use the second part",
        ),
    ]

    def tests(self):
        return [
        ]
