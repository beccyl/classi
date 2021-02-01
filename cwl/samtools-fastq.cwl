#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
label: 'SamTools: Fastq'
doc: |-
  Converts a BAM or CRAM into either FASTQ or FASTA format depending on the command invoked.
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

          n*i*    ignore the left part of the tag until the separator, then use the second part

requirements:
- class: ShellCommandRequirement
- class: InlineJavascriptRequirement
- class: DockerRequirement
  dockerPull: |-
    quay.io/biocontainers/samtools@sha256:3883c91317e7b6b62e31c82e2cef3cc1f3a9862633a13f850a944e828dd165ec

inputs:
- id: omitReadNumbers
  label: omitReadNumbers
  doc: |-
    Don't append /1 and /2 to the read name. By default, either '/1' or '/2' is added to the end of read names  where  the  corresponding BAM_READ1 or BAM_READ2 flag is set.  Using -n causes read names to be left as they are.
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: -n
- id: appendReadNumbers
  label: appendReadNumbers
  doc: |-
    Always add either '/1' or '/2' to the end of read names even when put into different files.
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: -N
- id: outputQuality
  label: outputQuality
  doc: |-
    Use quality values from OQ tags in preference to standard quality string if available.
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: -O
- id: copyTags
  label: copyTags
  doc: Copy RG, BC and QT tags to the FASTQ header line.
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: -t
- id: requireAllFlagSet
  label: requireAllFlagSet
  doc: |-
    Only output alignments with all bits set in INT present in the FLAG field.  INT can be specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with `0' (i.e. /^0[0-7]+/) [0].
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -f
- id: excludeAnyFlagSet
  label: excludeAnyFlagSet
  doc: |-
    Do not output alignments with ANY bits set in INT present in the FLAG field.  INT can be specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with `0' (i.e. /^0[0-7]+/) [0].
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -F
- id: excludeAllFlagSet
  label: excludeAllFlagSet
  doc: |-
    Only EXCLUDE reads with ALL bits set in INT present in the FLAG field.  INT can be specified  in hex by beginning with `0x' (i.e. /^0x[0-9A-F]+/) or in octal by beginning with `0' (i.e. /^0[0-7]+/) [0].
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -G
- id: nonspecificFilename
  label: nonspecificFilename
  doc: write paired reads flagged both or neither READ1 and READ2 to FILE
  type:
  - string
  - 'null'
  default: generated-_R0.fastq
  inputBinding:
    prefix: '-0'
    valueFrom: $(inputs.bam.basename.replace(/.bam$/, ""))-_R0.fastq
- id: read1Filename
  label: read1Filename
  doc: write paired reads flagged READ1 to FILE
  type:
  - string
  - 'null'
  default: generated-_R1.fastq
  inputBinding:
    prefix: '-1'
    valueFrom: $(inputs.bam.basename.replace(/.bam$/, ""))-_R1.fastq
- id: read2Filename
  label: read2Filename
  doc: write paired reads flagged READ2 to FILE
  type:
  - string
  - 'null'
  default: generated-_R2.fastq
  inputBinding:
    prefix: '-2'
    valueFrom: $(inputs.bam.basename.replace(/.bam$/, ""))-_R2.fastq
- id: singletonFilename
  label: singletonFilename
  doc: write singleton reads to FILE [assume single-end]
  type:
  - string
  - 'null'
  default: generated-_S.fastq
  inputBinding:
    prefix: -s
    valueFrom: $(inputs.bam.basename.replace(/.bam$/, ""))-_S.fastq
- id: defaultQualityScore
  label: defaultQualityScore
  doc: default quality score if not given in file [1]
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -v
- id: barcodeTag
  label: barcodeTag
  doc: 'aux tag to find index reads in [default: BC]'
  type:
  - string
  - 'null'
  inputBinding:
    prefix: --barcode-tag
- id: qualityTag
  label: qualityTag
  doc: 'aux tag to find index quality in [default: QT]'
  type:
  - string
  - 'null'
  inputBinding:
    prefix: --quality-tag
- id: indexFormat
  label: indexFormat
  doc: |-
    string to describe how to parse the barcode and quality tags. For example: i14i8   the first 14 characters are index 1, the next 8 characters are index 2.  n8i14   ignore the first 8 characters, and use the next 14 characters for index 1.  If the tag contains a separator, then the numeric part can be replaced with  '*'  tomean 'read until the separator or end of tag', for example: n*i*    ignore the left part of the tag until the separator, then use the second part
  type:
  - string
  - 'null'
  inputBinding:
    prefix: --index-format
- id: bam
  label: bam
  type: File
  inputBinding:
    position: 10
- id: threads
  label: threads
  doc: Number of additional threads to use [0].
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -@
    position: 5

outputs:
- id: out
  label: out
  type: stdout
- id: nonspecific
  label: nonspecific
  type:
  - File
  - 'null'
  outputBinding:
    glob: $(inputs.bam.basename.replace(/.bam$/, ""))-_R0.fastq
    loadContents: false
- id: read1
  label: read1
  type:
  - File
  - 'null'
  outputBinding:
    glob: $(inputs.bam.basename.replace(/.bam$/, ""))-_R1.fastq
    loadContents: false
- id: read2
  label: read2
  type:
  - File
  - 'null'
  outputBinding:
    glob: $(inputs.bam.basename.replace(/.bam$/, ""))-_R2.fastq
    loadContents: false
- id: singleton
  label: singleton
  type:
  - File
  - 'null'
  outputBinding:
    glob: $(inputs.bam.basename.replace(/.bam$/, ""))-_S.fastq
    loadContents: false
stdout: _stdout
stderr: _stderr

baseCommand:
- samtools
- fastq
arguments: []

hints:
- class: ToolTimeLimit
  timelimit: |-
    $([inputs.runtime_seconds, 86400].filter(function (inner) { return inner != null })[0])
id: SamToolsFastq
$schemas:
  - 'http://dublincore.org/2012/06/14/dcterms.rdf'
  - 'http://xmlns.com/foaf/spec/20140114.rdf'
  - 'https://schema.org/docs/schema_org_rdfa.html'
's:author':
  - class: 's:Person'
    's:email': 'mailto:rebecca.louise.evans@gmail.com'
    's:identifier': 'https://orcid.org/0000-0002-4923-0662'
    's:name': Rebecca Evans
's:codeRepository': 'https://github.com/beccyl/classi'
's:dateCreated': '2021-01-12'
