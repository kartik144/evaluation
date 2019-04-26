# Bilingual Evaluation Understudy (BLEU)

BLEU (bilingual evaluation understudy) is an algorithm for evaluating the quality of text which has been 
machine-translated from one natural language to another.

This repository contains a python script to perform compare machine translation outputs at sentence level using the BLEU
metric.

All the dependencies of the script can be met by installing the CONDA environment using the YAML file provided.

To run the script, use the following command:
```bash
$ python3 bleu.py -N [integer/list] --input [path] --reference [path] -T [float(0-1)]
```
where the command line arguments are:
```
-N          :   the n-grams to be used. This could be either a single integer or a list of float values, which would 
                signify that a weighted scheme is to be followed to calculate the BLEU score
                
--input     :   Path to input file

--reference :   Path to reference file

-T          :   Treshold to classify a translation as true positive
```

By default, it uses unigrams to calculate the BLEU score.

Example:
```bash
$ python3 bleu.py -N 2          # this would generate the BLEU scores using bi-grams only
$ python3 bleu.py -N 0.5,0.5    # this would generate the BLEU scores using unigrams and bi-grams giving equal weights to both the individual scores of unigrams and bigrams
```
