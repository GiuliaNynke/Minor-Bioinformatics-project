#############################################
### import, naming files and naming lists ###
#############################################
import Bio
from Bio import SeqIO
inputfile = "MERS_CoV.fasta"
new_file = "MERS_CoV_filtered.fasta"
names = []
sequences = []

########################################################################
### making a list for the names and sequences from the original file ###
########################################################################
with open (inputfile, 'r') as file:
    for lines in SeqIO.parse(file, "fasta"):
        sequences.append(lines.seq)

with open (inputfile, 'r') as file:
    for line in file:
        if ">" in line:
            names.append(line.rstrip())
#print(names)
#print(sequences)

############################################################################
### remove all sequences with 'partial genome' and 'related' in the name ###
############################################################################
f =open(new_file, 'w')
i = 0
while i != len(names):
    if "partial genome" in names[i]:
        print (str(i) + " no")
        i = i + 1
    elif "related" in names[i]:
        print (str(i) + " no")
        i = i + 1
    else:
        f.write(str(names[i]) + "\n" + str(sequences[i]) + "\n")
        i = i + 1
