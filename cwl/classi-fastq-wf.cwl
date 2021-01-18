class: Workflow
cwlVersion: v1.0
id: classi_fastq_wf
label: 'Classi: fastq to squeakr workflow'
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
  s: https://schema.org/

$schemas:
- http://dublincore.org/2012/06/14/dcterms.rdf
- http://xmlns.com/foaf/spec/20140114.rdf
- https://schema.org/docs/schema_org_rdfa.html

inputs:
  - id: kmer-size
    type: int
    'sbg:x': -967.810791015625
    'sbg:y': -463.2329406738281
  - id: input
    'sbg:fileTypes': .fastq
    type: 'File[]'
    'sbg:x': -1012.796875
    'sbg:y': -168
outputs:
  - id: output
    outputSource:
      - squeakr_count/output
    type: File
    'sbg:x': -274.2442321777344
    'sbg:y': -244.67098999023438
steps:
  - id: lognumslots_tool
    in:
      - id: ntcard-hist
        source: ntcard_tool/output
    out:
      - id: output
    run: ./lognumslots.cwl
    label: 'lognumslots: script'
    'sbg:x': -575.1642456054688
    'sbg:y': -375.5325927734375
  - id: ntcard_tool
    in:
      - id: threads
        default: 1
      - id: k-size
        default: 32
        source: kmer-size
      - id: prefix
        default: ./
      - id: input
        source:
          - input
    out:
      - id: output
    run: ./ntcard.cwl
    label: NtCard
    'sbg:x': -797.008544921875
    'sbg:y': -282
  - id: squeakr_count
    in:
      - id: k-size
        source: kmer-size
      - id: cutoff
        default: 3
      - id: log-slots
        source: lognumslots_tool/output
      - id: input-files
        source:
          - input
      - id: out-file
        default: ./output.squeakr
    out:
      - id: output
    run: ./squeakr-count.cwl
    label: squeakr-count
    'sbg:x': -450.1314697265625
    'sbg:y': -245.63128662109375
requirements: []
's:author':
  - class: 's:Person'
    's:email': 'mailto:rebecca.louise.evans@gmail.com'
    's:identifier': 'https://orcid.org/0000-0002-4923-0662'
    's:name': 'Rebecca Evans'
's:codeRepository': 'https://github.com/beccyl/classi'
's:dateCreated': '2021-01-12'
