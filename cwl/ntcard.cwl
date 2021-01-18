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

id: ntcard_tool
baseCommand:
  - ntcard
inputs:
  - 'sbg:toolDefaultValue': '4'
    id: threads
    type: int
    inputBinding:
      position: 0
      prefix: '-t'
  - 'sbg:toolDefaultValue': '32'
    id: k-size
    type: int
    inputBinding:
      position: 0
      prefix: '-k'
    label: kmer size
  - id: prefix
    type: string
    inputBinding:
      position: 0
      prefix: '-p'
  - id: input
    type: 'File[]'
    inputBinding:
      position: 10
    'sbg:fileTypes': .fastq
outputs:
  - id: output
    type: File
    outputBinding:
      glob: '*.hist'
label: ntcard-tool
requirements:
  - class: ResourceRequirement
    coresMin: 0
  - class: DockerRequirement
    dockerPull: beccyl/ntcard
  - class: InlineJavascriptRequirement

s:author:
  - class: s:Person
    s:identifier: https://orcid.org/0000-0002-4923-0662
    s:email: mailto:rebecca.louise.evans@gmail.com
    s:name: Rebecca Evans

s:codeRepository: https://github.com/beccyl/classi
s:dateCreated: "2021-01-12"
