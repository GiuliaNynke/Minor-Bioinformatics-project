##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
output_file_forward_primer_c1 = "Filtered_forward_primers_cluster1.txt"
output_file_reverse_primer_c1 = "Filtered_reverse_primers_cluster1.txt"
temporary_list_forward = []
temporary_list_reverse = []
output_list_forward = []
output_list_reverse = []
output_file_forward = "forward_primers_cluster1_filtered.txt"
output_file_reverse= "reverse_primers_cluster1_filtered.txt"

##################################################
### open the forward primers file of cluster 1 ###
##################################################
with open (output_file_forward_primer_c1, 'r') as file:
    for line in file:
        if "Primers" in line:
            print ("name")
        elif "Sequence" in line:
            print ("name")
        else:
            temporary_list_forward.append(line.split())

print (temporary_list_forward)

#########################################
### remove all forward primer doubles ###
#########################################
for list_line in temporary_list_forward:
    if list_line not in output_list_forward:
        output_list_forward.append(list_line)
print(output_list_forward)

######################################################
### write all unique forward primers to a new file ###
######################################################
n = (len(output_list_forward))
i=0
f = open(output_file_forward, 'w')

f.write("Forward Primers \nStart \tSequence \t\tLength \tGC% \tTm \tAny_th \tEnd_th \tHpin \tQuality  \n")
while i != n:
    f.write (str(output_list_forward[i])+ "\n")
    i = i+1

f.close()

##################################################
### open the reverse primers file of cluster 1 ###
##################################################
with open (output_file_reverse_primer_c1, 'r') as file:
    for line in file:
        if "Primers" in line:
            print ("name")
        elif "Sequence" in line:
            print ("name")
        else:
            temporary_list_reverse.append(line.split())

print (temporary_list_reverse)

#########################################
### remove all reverse primer doubles ###
#########################################
for list_line in temporary_list_reverse:
    if list_line not in output_list_reverse:
        output_list_reverse.append(list_line)
print(output_list_reverse)

######################################################
### write all unique reverse primers to a new file ###
######################################################
n = (len(output_list_reverse))
i=0
f = open(output_file_reverse, 'w')

f.write("Forward Primers \nStart \tSequence \t\tLength \tGC% \tTm \tAny_th \tEnd_th \tHpin \tQuality  \n")
while i != n:
    f.write (str(output_list_reverse[i])+ "\n")
    i = i+1

f.close()
