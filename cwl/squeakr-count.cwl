#!/usr/bin/env cwl-runner
class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
  s: https://schema.org/

$schemas:
- http://dublincore.org/2012/06/14/dcterms.rdf
- http://xmlns.com/foaf/spec/20140114.rdf
- https://schema.org/docs/schema_org_rdfa.html

id: squeakr_count
baseCommand:
  - squeakr
  - count
inputs:
  - 'sbg:toolDefaultValue': '32'
    id: k-size
    type: int
    inputBinding:
      position: 0
      prefix: '-k'
    label: kmer size
    doc: max kmer size is 32 for exact mode
  - 'sbg:toolDefaultValue': '3'
    id: cutoff
    type: int?
    inputBinding:
      position: 0
      prefix: '-c'
    label: cutoff
    doc: Suggested cutoff is related to input file size
  - id: log-slots
    type: int?
    inputBinding:
      position: 0
      prefix: '-s'
    label: log-slots
    doc: value estimated from ntcard
  - id: input-files
    type: 'File[]'
    inputBinding:
      position: 10
    label: files
    doc: fastq or fastq.gz
    'sbg:fileTypes': '.fastq, .fastq.gz'
  - id: exact
    type: boolean?
    inputBinding:
      position: 0
      prefix: '-e'
  - id: no-counts
    type: boolean?
    inputBinding:
      position: 0
      prefix: '-n'
  - 'sbg:toolDefaultValue': '1'
    id: threads
    type: int?
    inputBinding:
      position: 0
      prefix: '-t'
    label: num-threads
    doc: number of threads to use to count (default = number of hardware threads)
  - 'sbg:toolDefaultValue': ./output.squeakr
    id: out-file
    type: string
    inputBinding:
      position: 9
      prefix: '-o'
    default: output.squeakr
    label: out-file
    doc: file in which output should be written
outputs:
  - id: output
    type: File
    outputBinding:
      glob: output.squeakr
label: squeakr-count
requirements:
  - class: ResourceRequirement
    coresMin: 1
  - class: DockerRequirement
    dockerPull: 'beccyl/squeakr:master_0d58134'
  - class: InlineJavascriptRequirement
's:author':
  - class: 's:Person'
    's:email': 'mailto:rebecca.louise.evans@gmail.com'
    's:identifier': 'https://orcid.org/0000-0002-4923-0662'
    's:name': Rebecca Evans
's:codeRepository': 'https://github.com/beccyl/classi'
's:dateCreated': '2021-01-12'
