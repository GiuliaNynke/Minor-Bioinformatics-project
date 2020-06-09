##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
outputname_cluster2 = "MERS_CoV_cluster2.fasta"
outputname_muscle = "MERS_CoV_cluster1_aligned.fasta"
outputname_cluster1_replaced = "MERS_CoV_cluster1_replaced.fasta"
outputname_cluster2_replaced = "MERS_CoV_cluster2_replaced.fasta"
inputname_primer3_cluster1 = "MERS_CoV_cluster1_input_primer3.txt"
inputname_primer3_cluster2 = "MERS_CoV_cluster2_input_primer3.txt"
sequences_aligned_cluster1 = []
names_aligned_cluster1 = []
sequences_aligned_cluster2 = []
names_aligned_cluster2 = []
primer_task= 'generic'
P3_flag= '1'
left_primer= '1'
right_primer= '1'
internal_oligo= '0'
opt_size= '20'
min_size= '18'
max_size= '22'
liberal_base= '1'

#########################
### replacing - for N ###
#########################
f1 = open (outputname_cluster1_replaced, 'w')
f2 = open (outputname_cluster2_replaced, 'w')

with open (outputname_muscle, 'r') as file1:
    for line in file1:
        line = line.replace("-", "N")
        print (line)
        f1.write(line)

with open (outputname_cluster2, 'r') as file2:
    for line in file2:
        line = line.replace("-", "N")
        print (line)
        f2.write(line)

f1.close()
f2.close()

######################################################
### putting names and sequences in different lists ###
######################################################
with open (outputname_cluster1_replaced, 'r') as file1:
    for lines in SeqIO.parse(file1, "fasta"):
        sequences_aligned_cluster1.append(lines.seq)
        names_aligned_cluster1.append(lines.id)

with open (outputname_cluster2_replaced, 'r') as file2:
    for lines in SeqIO.parse(file2, "fasta"):
        sequences_aligned_cluster2.append(lines.seq)
        names_aligned_cluster2.append(lines.id)

########################################################
### making a dictionary with the names and sequences ###
########################################################
dictionary1 = dict(zip(names_aligned_cluster1,sequences_aligned_cluster1))
dictionary2 = dict(zip(names_aligned_cluster2,sequences_aligned_cluster2))
print (dictionary1)
print (dictionary2)

#####################################
### making the primer3 input file ###
#####################################
# adding flags to the primer3 input file
n = 0
m = 0
f1 = open(inputname_primer3_cluster1, 'w')
f1.write("PRIMER_TASK="+primer_task+'\n'+"P3_FILE_FLAG="+P3_flag+'\n'+"PRIMER_PICK_LEFT_PRIMER="+left_primer+'\n'+"PRIMER_PICK_RIGHT_PRIMER="+right_primer+'\n'+"PRIMER_PICK_INTERNAL_OLIGO="+internal_oligo+'\n'+"PRIMER_OPT_SIZE="+opt_size+'\n'+"PRIMER_MIN_SIZE="+min_size+'\n'+"PRIMER_MAX_SIZE="+max_size+'\n'+"PRIMER_LIBERAL_BASE="+liberal_base+'\n'+ "="+'\n')
f2 = open(inputname_primer3_cluster2, 'w')
f2.write("PRIMER_TASK="+primer_task+'\n'+"P3_FILE_FLAG="+P3_flag+'\n'+"PRIMER_PICK_LEFT_PRIMER="+left_primer+'\n'+"PRIMER_PICK_RIGHT_PRIMER="+right_primer+'\n'+"PRIMER_PICK_INTERNAL_OLIGO="+internal_oligo+'\n'+"PRIMER_OPT_SIZE="+opt_size+'\n'+"PRIMER_MIN_SIZE="+min_size+'\n'+"PRIMER_MAX_SIZE="+max_size+'\n'+"PRIMER_LIBERAL_BASE="+liberal_base+'\n'+ "="+'\n')
# set sequences in primer3 format
for x in dictionary1:
    id = names_aligned_cluster1[n]
    f1.write("SEQUENCE_ID"+"=" + id + "\n")
    seq = sequences_aligned_cluster1[n]
    f1.write("SEQUENCE_TEMPLATE"+ "=" + str(seq) + "\n")
    f1.write("=" + "\n")
    n = n+1
for y in dictionary2:
    id = names_aligned_cluster2[m]
    f2.write("SEQUENCE_ID"+"=" + id + "\n")
    seq = sequences_aligned_cluster2[m]
    f2.write("SEQUENCE_TEMPLATE"+ "=" + str(seq) + "\n")
    f2.write("=" + "\n")
    m = m+1
f1.close()
f2.close()

