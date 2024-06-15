# 'Max Length' DNA Sequences Analysis

## Description
This Python script is designed to analyze DNA sequences from GenBank files. It provides two main analyses:

1. Duplicated Sequence Analysis: Finds and prints the longest repeated sequence within the DNA.
2. ORF Analysis: Finds and prints the longest open reading frame (ORF).

### Installing the dependencies:
The required packeges are in `requirements.txt`
```
pip install -r requirements.txt
```
## Usage
To use this script, you need to specify the input file and the type of analysis you want to perform. The input file should be in GenBank format.

## Command-line Arguments
--input (required): Path to the Fasta or GenBank file.
--duplicate: Perform the duplicated sequence analysis.
--ORF: Perform the ORF analysis.