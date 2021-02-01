class: Workflow
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
inputs:
  - id: bam_inputs
    type: 'File[]'
    'sbg:x': -223
    'sbg:y': 64
  - id: kmer-size
    type: int
    'sbg:exposed': true
  - id: cutoff
    type: int?
    'sbg:exposed': true
outputs:
  - id: out
    outputSource:
      - bamtosqueakr/out
    type: File
    'sbg:x': 150
    'sbg:y': 62
steps:
  - id: bamtosqueakr
    in:
      - id: inp
        linkMerge: merge_nested
        source: bam_inputs
      - id: kmer-size
        default: 32
        source: kmer-size
      - id: cutoff
        default: 3
        source: cutoff
    out:
      - id: out
    run: classi-bam-wf.cwl
    label: classi-bam-wf
    scatter:
      - inp
    scatterMethod: dotproduct
    'sbg:x': -45
    'sbg:y': 64
requirements:
  - class: SubworkflowFeatureRequirement
  - class: ScatterFeatureRequirement
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
