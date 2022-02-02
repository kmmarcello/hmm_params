---
title: "Anvio Phylogenomics Workflow"
author: "Kaylah Marcello"
date: "2/2/2022"
output: 
  html_document: 
    keep_md: yes
---


These are the websites and workflows I used:

[Anvio phylogenomics workflow](https://merenlab.org/2017/06/07/phylogenomics/)  
[Making your own HMM database](https://merenlab.org/2016/05/21/archaeal-single-copy-genes/)  
[HMM hits Matrix](https://anvio.org/help/main/programs/anvi-script-gen-hmm-hits-matrix-across-genomes/)  
[EggNOG database](http://eggnog5.embl.de/#/app/results)

## Making HMM file for Anvi'o (x3)
***
Custom HMM folder contains:  
genes.hmm.gz - concatenated hmm profiles from EggNOG  
genes.txt - list of genes + accession + source  
kind.txt - gene  
target.txt - AA:GENE  
noise_cutoff_terms.txt -E 1e-30  

### Anvi'o
hope (v7.1)  

### Pre analysis - reformat fasta file names:
### 1. Convert to an "improved" fasta header, saves file-name-key in a tsv

```r
anvi-script-reformat-fasta -c contigs.fa 
                           -o contigs-fixed.fa -l 0 
                           --simplify-names 
                           --report-files contigs.tsv
```

### 2. Generate an anvio-ready genome database (.db) and run HMMS  

```bash
for i in `ls *fa | awk 'BEGIN{FS=".fa"}{print $1}'`
do
  anvi-gen-contigs-database -f $i.fa -o $i.db -T 4
done
```
## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:


```r
summary(cars)
```

```
##      speed           dist       
##  Min.   : 4.0   Min.   :  2.00  
##  1st Qu.:12.0   1st Qu.: 26.00  
##  Median :15.0   Median : 36.00  
##  Mean   :15.4   Mean   : 42.98  
##  3rd Qu.:19.0   3rd Qu.: 56.00  
##  Max.   :25.0   Max.   :120.00
```

## Including Plots

You can also embed plots, for example:

![](anvio-phylo-workflow_files/figure-html/pressure-1.png)<!-- -->

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
