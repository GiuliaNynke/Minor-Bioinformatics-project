#############################################
### import, naming files and naming lists ###
#############################################
import Bio
from Bio import SeqIO
inputfile = "MERS_CoV_clustered.fasta"
outputfile_cluster1 = "MERS_CoV_cluster1.fasta"
outputfile_cluster2 = "MERS_CoV_cluster2.fasta"
names = []
sequences = []
clusters =[]

########################################################################
### making a list for the names and sequences from the original file ###
########################################################################
#list for sequences
with open (inputfile, 'r') as file:
    for lines in SeqIO.parse(file, "fasta"):
        sequences.append(lines.seq)

#list for names
with open (inputfile, 'r') as file:
    for line in file:
        if ">" in line:
            names.append(line.rstrip())

############################################
### making a list of the cluster centers ###
############################################
for cluster in names:
    if "cluster_center=True" in cluster:
        clusters = clusters + cluster.split()
#print(clusters)

#################################
### make one file per cluster ###
#################################
#open new files
f1 = open(outputfile_cluster1, 'w')
f2 = open(outputfile_cluster2, 'w')

#write the names and sequences in the new files
i = 0
while i != len(names):
    if clusters[3] in names[i]:
        f1.write(str(names[i]) + "\n" + str(sequences[i]) + "\n")
        i = i + 1
    elif clusters[9] in names[i]:
        f2.write(str(names[i]) + "\n" + str(sequences[i]) + "\n")
        i = i + 1

#close the new files
f1.close()
f2.close()
