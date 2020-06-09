##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
outputname_sumaclust = "MERS_CoV_clustered.fasta"
outputname_cluster1 = "MERS_CoV_cluster1.fasta"
outputname_cluster2 = "MERS_CoV_cluster2.fasta"
names_clustered = []
sequences_clustered = []
clusters =[]

#######################################################################
### make a list for the names and sequences from the sumaclust file ###
#######################################################################
#list for sequences
with open (outputname_sumaclust, 'r') as file:
    for lines in SeqIO.parse(file, "fasta"):
        sequences_clustered.append(lines.seq)

#list for names
with open (outputname_sumaclust, 'r') as file:
    for line in file:
        if ">" in line:
            names_clustered.append(line.rstrip())

##########################################
### make a list of the cluster centers ###
##########################################
for cluster in names_clustered:
    if "cluster_center=True" in cluster:
        clusters = clusters + cluster.split()

#################################
### make one file per cluster ###
#################################
#open new files
f1 = open(outputname_cluster1, 'w')
f2 = open(outputname_cluster2, 'w')

#write the names and sequences in the new files
i = 0
while i != len(names_clustered):
    if clusters[3] in names_clustered[i]:
        f1.write(str(names_clustered[i]) + "\n" + str(sequences_clustered[i]) + "\n")
        i = i + 1
    elif clusters[9] in names_clustered[i]:
        f2.write(str(names_clustered[i]) + "\n" + str(sequences_clustered[i]) + "\n")
        i = i + 1

#close the new files
f1.close()
f2.close()

