#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
label: 'Squeakr: Count'
doc: |2

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

requirements:
- class: ShellCommandRequirement
- class: InlineJavascriptRequirement
- class: DockerRequirement
  dockerPull: |-
    beccyl/squeakr@sha256:afae10fe6feff0e4cb872d698bf779826dfe7adbbee9a309f4c7abe3ee1b7d67

inputs:
- id: exact
  label: exact
  doc: |-
    (-e)  squeakr-exact (default is Squeakr approximate). Possible values: {true, false}
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: --exact
    separate: true
- id: kmer_size
  label: kmer_size
  doc: (-k)  <k-size> length of k-mers to count. Required.
  type: int
  inputBinding:
    prefix: -k
    separate: true
- id: cutoff
  label: cutoff
  doc: |-
    (-c)  <cutoff> only output k-mers with count greater than or equal to cutoff (default = 1).  Optional.
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -c
    separate: true
- id: no_counts
  label: no_counts
  doc: |-
    (-n)  only output k-mers and no counts (default = false). Possible values: {true, false}
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: --no-counts
    separate: true
- id: log_slots
  label: log_slots
  doc: |-
    (-s)  <log-slots> log of number of slots in the CQF. (Size argument is only optional when numthreads is exactly 1.)
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -s
    separate: true
- id: num_threads
  label: num_threads
  doc: (-t)  number of threads to use to count (default = number of hardware threads).
  type:
  - int
  - 'null'
  inputBinding:
    prefix: -t
    separate: true
- id: input_list
  label: input_list
  doc: (-i)  file containing list of input filters. Required.
  type:
    type: array
    items: File
  inputBinding:
    position: 10
- id: out_file
  label: out_file
  doc: (-o)  file in which output should be written. Required.
  type:
  - string
  - 'null'
  default: ./output.squeakr
  inputBinding:
    prefix: -o
    position: 9
    separate: true

outputs:
- id: out
  label: out
  type: File
  outputBinding:
    glob: ./output.squeakr
    loadContents: false
stdout: _stdout
stderr: _stderr

baseCommand:
- squeakr
- count
arguments: []

hints:
- class: ToolTimeLimit
  timelimit: |-
    $([inputs.runtime_seconds, 86400].filter(function (inner) { return inner != null })[0])
id: SqueakrCount
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
