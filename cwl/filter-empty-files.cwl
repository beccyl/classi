#!/usr/bin/env cwl-runner
class: ExpressionTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
  s: https://schema.org/

$schemas:
- http://dublincore.org/2012/06/14/dcterms.rdf
- http://xmlns.com/foaf/spec/20140114.rdf
- https://schema.org/docs/schema_org_rdfa.html

id: filter-empty-files
inputs:
  - id: infiles
    type: 'File[]'
outputs:
  - id: outfiles
    type: 'File[]'
label: filter-empty-files
requirements:
  - class: InlineJavascriptRequirement
expression: |
  ${
      var files = [];
      for (var i = 0; i < inputs.infiles.length; i++) {
        var file = inputs.infiles[i];
        if (file.size > 0) {
          files.push(file);
        }
      }
      return {"outfiles": files};
  }

s:author:
  - class: s:Person
    s:identifier: https://orcid.org/0000-0002-4923-0662
    s:email: mailto:rebecca.louise.evans@gmail.com
    s:name: Rebecca Evans

s:codeRepository: https://github.com/beccyl/classi
s:dateCreated: "2021-01-12"
