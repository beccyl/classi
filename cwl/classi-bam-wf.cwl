class: Workflow
cwlVersion: v1.0
id: classi_bam_wf
label: classi-bam-wf
$namespaces:
  s: 'https://schema.org/'
  sbg: 'https://www.sevenbridges.com/'
inputs:
  - id: inp
    type: File
    'sbg:x': -325
    'sbg:y': -14
  - id: kmer-size
    type: int
    'sbg:exposed': true
  - id: cutoff
    type: int?
    'sbg:exposed': true
outputs:
  - id: out
    outputSource:
      - classi_fastq_wf/out
    type: File
    'sbg:x': 368
    'sbg:y': -16
steps:
  - id: filter-empty-files
    in:
      - id: infiles
        linkMerge: merge_flattened
        source:
          - _gatk_sam_to_fastq/out
    out:
      - id: outfiles
    run: ./filter-empty-files.cwl
    label: FilterEmptyFiles
    'sbg:x': 18.8763370513916
    'sbg:y': -14.035053253173828
  - id: classi_fastq_wf
    in:
      - id: kmer-size
        default: 32
        source: kmer-size
      - id: input
        source:
          - filter-empty-files/outfiles
      - id: cutoff
        default: 3
        source: cutoff
    out:
      - id: out
    run: ./classi-fastq-wf.cwl
    label: 'Classi: fastq to squeakr workflow'
    'sbg:x': 197
    'sbg:y': -14.042083740234375
  - id: _gatk_sam_to_fastq
    in:
      - id: inp
        source: inp
      - id: validation_stringency
        default: LENIENT
    out:
      - id: out
    run: ./gatk-samtofastq.cwl
    label: 'Gatk4: SamToFastq'
    'sbg:x': -153
    'sbg:y': -14
requirements:
  - class: SubworkflowFeatureRequirement
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
's:dateCreated': '2021-02-01'
