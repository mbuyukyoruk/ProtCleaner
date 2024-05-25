import argparse
import sys
import os
import subprocess
import textwrap

try:
    from Bio import SeqIO
except ImportError as e:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except ImportError as e:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python ProtCleaner.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

    Author: Murat Buyukyoruk

        ProtCleaner help:

This script is developed to remove protein sequences that contains ambiguous residues (i.e., X) that might be generated due to ambiguous characters in a DNA sequence such as N. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python ProtCleaner.py -i demo.fasta -l demo_sub_list.txt -o demo_sub_list.fasta

ProtCleaner dependencies:
	Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download
	tqdm                                                refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file containing protein sequences.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.


      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a original fasta file.\n')

results = parser.parse_args()
filename = results.filename
name_of_file, extension_of_file = os.path.splitext(filename)
out = name_of_file + "_cleaned" + extension_of_file

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text = True)
length = int(proc.communicate()[0].split('\n')[0])

f = open(out, 'a')
sys.stdout = f

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Reading...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        if "X" not in str(record.seq):
            print(record.format("fasta"))


