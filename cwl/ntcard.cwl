#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
label: ntcard
doc: |-
  ntCard is a streaming algorithm for estimating the frequencies of k-mers in genomics datasets. At its core, ntCard uses the ntHash algorithm to efficiently compute hash values for streamed sequences. It then samples the calculated hash values to build a reduced representation multiplicity table describing the sample distribution. Finally, it uses a statistical model to reconstruct the population distribution from the sample distribution.

requirements:
- class: ShellCommandRequirement
- class: InlineJavascriptRequirement
- class: DockerRequirement
  dockerPull: |-
    beccyl/ntcard@sha256:5da1f0266c6eac01a41b5dcde4cf2160e73618e197446e38f9d0f34586559d2c

inputs:
- id: files
  label: files
  doc: |-
    Acceptable file formats: fastq, fasta, sam, bam and in compressed formats gz, bz, zip, xz. 
  type:
    type: array
    items: File
  inputBinding:
    position: 10
- id: cov
  label: cov
  doc: (--cov=N)  the maximum coverage of kmer in output [1000]
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -c
- id: gap
  label: gap
  doc: |-
    (--gap=N)  the length of gap in the gap seed [0]. g mod 2 must equal k mod 2 unless g == 0. -g does not support multiple k currently.
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -g
- id: kmer
  label: kmer
  doc: (--kmer=N)  the length of kmer. Required.
  type: int
  inputBinding:
    prefix: -k
- id: threads
  label: threads
  doc: |-
    (--threads=N)  use N parallel threads [1] (N>=2 should be used when input files are >=2)
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -t
- id: prefix
  label: prefix
  doc: (--prefix=STRING)  the prefix for output file name(s)
  type:
  - string
  - 'null'
  inputBinding:
    prefix: -p
- id: outputFilename
  label: outputFilename
  doc: |-
    (--output=STRING)  the name for output file name (used when output should be a single file)
  type:
  - string
  - 'null'
  inputBinding:
    prefix: -o
- id: help
  label: help
  doc: (--help)  display this help and exit
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: --help
- id: version
  label: version
  doc: (--version)  output version information and exit
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: --version

outputs:
- id: out
  label: out
  type: File
  outputBinding:
    glob: '*.hist'
    loadContents: false
stdout: _stdout
stderr: _stderr

baseCommand:
- ntcard
arguments: []

hints:
- class: ToolTimeLimit
  timelimit: |-
    $([inputs.runtime_seconds, 86400].filter(function (inner) { return inner != null })[0])
id: ntcard
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
