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
id: lognumslots_tool
baseCommand:
  - lognumslots.sh
inputs:
  - id: ntcard-hist
    type: File
    inputBinding:
      position: 1
outputs:
  - id: output
    type: int
    outputBinding:
      loadContents: true
      glob: _stdout
      outputEval: '$(parseInt(self[0].contents,10))'
label: lognumslots-tool
requirements:
  - class: ResourceRequirement
    coresMin: 1
  - class: DockerRequirement
    dockerPull: 'beccyl/squeakr:master_0d58134'
  - class: InlineJavascriptRequirement
stdout: _stdout

s:author:
  - class: s:Person
    s:identifier: https://orcid.org/0000-0002-4923-0662
    s:email: mailto:rebecca.louise.evans@gmail.com
    s:name: Rebecca Evans

s:codeRepository: https://github.com/beccyl/classi
s:dateCreated: "2021-01-12"
