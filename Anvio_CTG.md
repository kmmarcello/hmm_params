---
title: "Anvio_CTG"
author: "Kaylah Marcello"
date: "1/24/2022"
output: 
  html_document: 
    keep_md: yes
---


## Conceptual steps


```r
library("tidyverse")
library("janitor")
library("skimr")
```


```r
cyanobacteria_metadata <- readr::read_csv("data/Cyano_wholegenome_metadata.csv")
```

```
## New names:
## * `` -> ...22
## * `` -> ...23
```

```
## Rows: 193 Columns: 23
```

```
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (21): GenBank Assembly ID (Accession.version), RefSeq Assembly ID (Acces...
## dbl  (2): GenBank release ID, UIDs
```

```
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```


```r
skim(cyanobacteria_metadata)
```


Table: Data summary

|                         |                       |
|:------------------------|:----------------------|
|Name                     |cyanobacteria_metadata |
|Number of rows           |193                    |
|Number of columns        |23                     |
|_______________________  |                       |
|Column type frequency:   |                       |
|character                |21                     |
|numeric                  |2                      |
|________________________ |                       |
|Group variables          |None                   |


**Variable type: character**

|skim_variable                           | n_missing| complete_rate| min| max| empty| n_unique| whitespace|
|:---------------------------------------|---------:|-------------:|---:|---:|-----:|--------:|----------:|
|GenBank Assembly ID (Accession.version) |         2|          0.99|   3|  15|     0|      191|          0|
|RefSeq Assembly ID (Accession.version)  |         6|          0.97|   3|  15|     0|      184|          0|
|RefSeq release ID                       |         6|          0.97|   3|   8|     0|      184|          0|
|Accession #                             |         6|          0.97|   8|  19|     0|      186|          0|
|Organism                                |         6|          0.97|  15|  73|     0|      183|          0|
|Genus                                   |       170|          0.12|   6|  19|     0|       19|          0|
|Species                                 |       168|          0.13|   6|  28|     0|       24|          0|
|Strain                                  |       171|          0.11|   3|  10|     0|       21|          0|
|environment                             |       181|          0.06|   5|   6|     0|        2|          0|
|Storage/Collection                      |       179|          0.07|   3|  80|     0|        6|          0|
|Regional Loaction                       |        82|          0.58|   3|  70|     0|       87|          0|
|geographic feature                      |       114|          0.41|   4|  81|     0|       65|          0|
|Environment Detail                      |        95|          0.51|   3| 120|     0|       77|          0|
|Tempurature                             |       175|          0.09|   4|  23|     0|       17|          0|
|Lat/Long                                |       144|          0.25|   7|  28|     0|       44|          0|
|Collection date                         |       145|          0.25|   4|  41|     0|       29|          0|
|NCBI taxonomy browser                   |         6|          0.97|  45| 114|     0|      184|          0|
|Primary Source                          |        56|          0.71|  23| 149|     0|      101|          0|
|Other source                            |       119|          0.38|  44| 100|     0|       74|          0|
|...22                                   |       158|          0.18|  44| 100|     0|       34|          0|
|...23                                   |       190|          0.02|  44|  46|     0|        3|          0|


**Variable type: numeric**

|skim_variable      | n_missing| complete_rate|    mean|      sd|    p0|    p25|     p50|      p75|     p100|hist  |
|:------------------|---------:|-------------:|-------:|-------:|-----:|------:|-------:|--------:|--------:|:-----|
|GenBank release ID |         6|          0.97| 7686917| 8722532|  8728| 502518| 3359378| 16043918| 23655148|▇▂▁▁▃ |
|UIDs               |         6|          0.97| 7652210| 8791496| 29508| 502758| 3389878| 16125133| 23759508|▇▂▁▁▃ |

