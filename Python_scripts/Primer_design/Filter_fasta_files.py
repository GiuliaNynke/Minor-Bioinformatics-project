##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
outputname_fasta_file = "MERS_CoV.fasta"
outputname_filter_fasta_file = "MERS_CoV_filtered.fasta"
names = []
sequences = []

###################################################################
### make a list for the names and sequences from the fasta file ###
###################################################################
#list for sequences
with open (outputname_fasta_file, 'r') as file:
    for lines in SeqIO.parse(file, "fasta"):
        sequences.append(lines.seq)

#list for names
with open (outputname_fasta_file, 'r') as file:
    for line in file:
        if ">" in line:
            names.append(line.rstrip())

############################################################################
### remove all sequences with 'partial genome' and 'related' in the name ###
############################################################################
#open new file
f =open(outputname_filter_fasta_file, 'w')

#filter the names and write the names and sequences to the new file
i = 0
while i != len(names):
    if "partial genome" in names[i]:
        i = i + 1
    elif "related" in names[i]:
        i = i + 1
    else:
        f.write(str(names[i]) + "\n" + str(sequences[i]) + "\n")
        i = i + 1

#close the new file
f.close

