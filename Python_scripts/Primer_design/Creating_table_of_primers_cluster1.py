##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
output_file_forward = "forward_primers_cluster1_filtered.txt"
output_file_reverse= "reverse_primers_cluster1_filtered.txt"
new_file_forward = 'forward_primers_cluster1_table.txt'
new_file_reverse = 'reverse_primers_cluster1_table.txt'
list_forward = []
list_reverse = []

###################################################################
### open the forward primers file of cluster 1 and make a table ###
###################################################################
with open (output_file_forward, 'r') as file:
    for line in file:
        line = line.replace("[", "")
        line = line.replace("'", "")
        line = line.replace("]", "")
        line = line.replace(",", "\t")
        list_forward.append(line)

print(list_forward)

i=0
f = open (new_file_forward, 'w')
while i != (len(list_forward)):
    f.write(list_forward[i])
    i = i+1
f.close()

###################################################################
### open the reverse primers file of cluster 1 and make a table ###
###################################################################
with open (output_file_reverse, 'r') as file:
    for line in file:
        line = line.replace("[", "")
        line = line.replace("'", "")
        line = line.replace("]", "")
        line = line.replace(",", "\t")
        list_reverse.append(line)

print(list_reverse)

i=0
f = open (new_file_reverse, 'w')
while i != (len(list_reverse)):
    f.write(list_reverse[i])
    i = i+1
f.close()
