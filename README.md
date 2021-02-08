# classi
CLoud Application Sequence-Search Index

Workflow for use in cloud environment.


Software / Other:
* [Common Workflow Language] (https://commonwl.org)
* [Janis] (https://janis.readthedocs.io/en/latest/)
* [Docker] (https://www.docker.com/)
* [cwltool] (https://github.com/common-workflow-language/cwltool)

To generate CWL for individual tools:
```
cd janis/tools
janis translate --name Gatk4SamToFastqLatest --output-dir ../../cwl __init__.py cwl
janis translate --name NtCardLatest --output-dir ../../cwl __init__.py cwl
janis translate --name SqueakrCountLatest --output-dir ../../cwl __init__.py cwl
janis translate --name MantisBuildLatest --output-dir ../../cwl __init__.py cwl
janis translate --name SamtoolsFastqLatest --output-dir ../../cwl __init__.py cwl
janis translate --name SamtoolsSortLatest --output-dir ../../cwl SamToolsSort cwl
```
* SamToolsSort is defined in janis.bioinformatics.tools
* RabixComposer does not support cwl v1.2, supports cwl v1.0 (rename the CWL version to v1.0 in generated files)

To generate CWL for the workflows:
```
cd janis/tools
janis translate --output-dir ../../cwl bam_to_squeakr_workflow.py cwl
janis translate --output-dir ../../cwl fastq_to_squeakr_workflow.py cwl
```

Use of the workflow in cloud environment.  Take note of scatter inputs.

## Workflows
### Fastq to squeakr
Base workflow - converts fastq input to a squeakr output
![](https://github.com/beccyl/classi/blob/main/docs/img/fastq_to_squeakr.jpg "Fastq to Squeakr Workfow")

### Bam to squeakr
Builds on base workflow.  Convert bam to fastq then pass through above workflow.
![](https://github.com/beccyl/classi/blob/main/docs/img/bam_to_squeakr.jpg "Bam to Squeakr Workfow")

### Scatter Bam inputs
Scatter Bam inputs - to run multiple bam inputs in parallel.
![](https://github.com/beccyl/classi/blob/main/docs/img/scatter_bams.jpg "Scatter Workfow")


## References:

```
@article{doi:10.1093/bioinformatics/btx636,
author = {Pandey, Prashant and Bender, Michael A and Johnson, Rob and Patro, Rob},
title = {Squeakr: An Exact and Approximate k-mer Counting System},
journal = {Bioinformatics},
volume = {},
number = {},
pages = {btx636},
year = {2017},
doi = {10.1093/bioinformatics/btx636},
URL = { + http://dx.doi.org/10.1093/bioinformatics/btx636},
eprint = {/oup/backfile/content_public/journal/bioinformatics/pap/10.1093_bioinformatics_btx636/1/btx636.pdf}
}
```

```
@article{10.1093/bioinformatics/btw832,
author = {Mohamadi, Hamid and Khan, Hamza and Birol, Inanc},
title = "{ntCard: a streaming algorithm for cardinality estimation in genomics data}",
journal = {Bioinformatics},
volume = {33},
number = {9},
pages = {1324-1330},
year = {2017},
month = {01},
abstract = "{Many bioinformatics algorithms are designed for the analysis of sequences of some uniform length, conventionally referred to as k-mers. These include de Bruijn graph assembly methods and sequence alignment tools. An efficient algorithm to enumerate the number of unique k-mers, or even better, to build a histogram of k-mer frequencies would be desirable for these tools and their downstream analysis pipelines. Among other applications, estimated frequencies can be used to predict genome sizes, measure sequencing error rates, and tune runtime parameters  for analysis tools. However, calculating a k-mer histogram from large volumes of sequencing data is a challenging task. Here, we present ntCard, a streaming algorithm for estimating the frequencies of k-mers in genomics datasets. At its core, ntCard uses the ntHash algorithm to efficiently compute hash values for streamed sequences. It then samples the calculated hash values to build a reduced representation multiplicity table describing the sample distribution. Finally, it uses a statistical model to reconstruct the population distribution from the sample distribution. We have compared the performance of ntCard and other cardinality estimation algorithms. We used three datasets of 480 GB, 500 GB and 2.4 TB in size, where the first two representing whole genome shotgun sequencing experiments on the human genome and the last one on the white spruce genome. Results show ntCard estimates k-mer coverage frequencies \\&gt; 15× faster than the state-of-the-art algorithms, using similar amount of memory, and with higher accuracy rates. Thus,  our benchmarks demonstrate ntCard as a potentially enabling technology for large-scale genomics applications.ntCard is  written in C ++ and is released under the GPL license. It is freely available at https://github.com/bcgsc/ntCard. Supplementary data are available at Bioinformatics online.}",
issn = {1367-4803},
doi = {10.1093/bioinformatics/btw832},
url = {https://doi.org/10.1093/bioinformatics/btw832},
eprint = {https://academic.oup.com/bioinformatics/article-pdf/33/9/1324/25151243/btw832.pdf},
```

