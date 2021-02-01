#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
label: 'Mantis: Build'
doc: |2

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

requirements:
- class: ShellCommandRequirement
- class: InlineJavascriptRequirement
- class: DockerRequirement
  dockerPull: |-
    beccyl/mantis@sha256:d943b32a724ee15650cfb37edf795998a5c106fb6eae7c5c0c58dfc862a81164

inputs:
- id: eqclass_dist
  label: eqclass_dist
  doc: '(-e)  write the eqclass abundance distribution. Possible values: {true, false}'
  type:
  - boolean
  - 'null'
  inputBinding:
    prefix: --eqclass_dist
    separate: true
- id: log_slots
  label: log_slots
  doc: (-s)  log of number of slots in the output CQF.
  type: int
  inputBinding:
    prefix: -s
    separate: true
- id: input_list
  label: input_list
  doc: (-i)  file containing list of input filters. Required.
  type:
  - string
  - 'null'
  default: generated
  inputBinding:
    prefix: -i
    separate: true
- id: build_output
  label: build_output
  doc: (-o)  directory where results should be written. Required.
  type:
  - string
  - 'null'
  default: generated
  inputBinding:
    prefix: -o
    separate: true

outputs:
- id: out
  label: out
  type: Directory
  outputBinding:
    glob: generated
    loadContents: false
stdout: _stdout
stderr: _stderr

baseCommand:
- mantis
- build
arguments: []

hints:
- class: ToolTimeLimit
  timelimit: |-
    $([inputs.runtime_seconds, 86400].filter(function (inner) { return inner != null })[0])
id: MantisBuild
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
