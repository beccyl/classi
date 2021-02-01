class: Workflow
cwlVersion: v1.0
id: classi_fastq_wf
label: 'Classi: fastq to squeakr workflow'
$namespaces:
  s: 'https://schema.org/'
  sbg: 'https://www.sevenbridges.com/'
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
  - id: cutoff
    type: int?
    'sbg:x': -827.8883056640625
    'sbg:y': -49.768821716308594
outputs:
  - id: out
    outputSource:
      - _squeakr_count/out
    type: File
    'sbg:x': -355.4664306640625
    'sbg:y': -175.11660766601562
steps:
  - id: nt_card
    in:
      - id: files
        source:
          - input
      - id: kmer
        source: kmer-size
      - id: prefix
        default: ./
    out:
      - id: out
    run: ./ntcard.cwl
    label: ntCard
    'sbg:x': -837.796875
    'sbg:y': -276.5
  - id: lognumslots_tool
    in:
      - id: ntcard-hist
        source: nt_card/out
    out:
      - id: output
    run: ./lognumslots.cwl
    label: lognumslots-tool
    'sbg:x': -574.793701171875
    'sbg:y': -374.5
  - id: _squeakr_count
    in:
      - id: exact
        default: true
      - id: kmer_size
        source: kmer-size
      - id: cutoff
        source: cutoff
      - id: no_counts
        default: true
      - id: log_slots
        source: lognumslots_tool/output
      - id: input_list
        source:
          - input
      - id: out_file
        default: ./output.squeakr
    out:
      - id: out
    run: ./squeakr-count.cwl
    label: 'Squeakr: Count'
    'sbg:x': -511.07171630859375
    'sbg:y': -174.55035400390625
requirements: []
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
