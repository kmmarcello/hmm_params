---
title: "Anvio Phylogenomics Workflow"
author: "Kaylah Marcello"
date: "2/2/2022"
output: 
  html_document: 
    keep_md: yes
---



Websites and workflows used:

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

### 2. Generate an anvio-ready genome database (.db)  

```bash
for i in `ls *fa | awk 'BEGIN{FS=".fa"}{print $1}'`
do
  anvi-gen-contigs-database -f $i.fa -o $i.db -T 4
done
```

### 3. Run HMMs from our own file, anvi-run-hmms

```bash
for i in `ls ./outputs/db/filamentous-subset/*db | awk 'BEGIN{FS=".fa"}{print $1}'`
do
  anvi-run-hmms -c $i --hmm-profile-dir hmms --just-do-it
done
```
