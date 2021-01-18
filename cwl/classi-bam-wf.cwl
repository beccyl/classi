class: Workflow
cwlVersion: v1.0
id: classi_bam2_wf
label: classi-bam2-wf
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
  s: https://schema.org/

$schemas:
- http://dublincore.org/2012/06/14/dcterms.rdf
- http://xmlns.com/foaf/spec/20140114.rdf
- https://schema.org/docs/schema_org_rdfa.html

inputs:
  - id: bam
    type: File
    'sbg:x': -488.1937561035156
    'sbg:y': -12.929893493652344
  - id: kmer-size
    type: int
    'sbg:exposed': true
outputs:
  - id: output
    outputSource:
      - classi_fastq_wf/output
    type: File
    'sbg:x': 319.0574645996094
    'sbg:y': -15.525801658630371
steps:
  - id: _sam_tools_fastq
    in:
      - id: bam
        source: _sam_tools_sort/out
    out:
      - id: out
      - id: nonspecific
      - id: read1
      - id: read2
      - id: singleton
    run: ./samtools-fastq.cwl
    label: 'SamTools: Fastq'
    'sbg:x': -188.0185089111328
    'sbg:y': -15.035053253173828
  - id: _sam_tools_sort
    in:
      - id: bam
        source: bam
    out:
      - id: out
    run: ./samtools-sort.cwl
    label: 'SamTools: Sort'
    'sbg:x': -353.1587219238281
    'sbg:y': -15.035053253173828
  - id: filter-empty-files
    in:
      - id: infiles
        source:
          - _sam_tools_fastq/read2
          - _sam_tools_fastq/singleton
          - _sam_tools_fastq/read1
          - _sam_tools_fastq/nonspecific
        linkMerge: merge_flattened
    out:
      - id: outfiles
    run: ./filter-empty-files.cwl
    label: FilterEmptyFiles
    'sbg:x': 18.8763370513916
    'sbg:y': -14.035053253173828
  - id: classi_fastq_wf
    in:
      - id: kmer-size
        source: kmer-size
      - id: input
        source:
          - filter-empty-files/outfiles
    out:
      - id: output
    run: ./classi-fastq-wf.cwl
    label: 'Classi: fastq to squeakr workflow'
    'sbg:x': 171.95034790039062
    'sbg:y': -13.595909118652344
requirements:
  - class: SubworkflowFeatureRequirement
  - class: MultipleInputFeatureRequirement
