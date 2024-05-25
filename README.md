# ProtCleaner

Author: Murat Buyukyoruk

ProtCleaner help:

This script is developed to remove protein sequences that contains ambiguous residues (i.e., X) that might be generated due to ambiguous characters in a DNA sequence such as N. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

    python ProtCleaner.py -i demo.fasta

ProtCleaner dependencies:

	Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download
	tqdm                                                refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file containing protein sequences.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.
