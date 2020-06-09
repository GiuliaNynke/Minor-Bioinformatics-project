##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
new_file_forward = 'forward_primers_cluster1_table.txt'
new_file_reverse = 'reverse_primers_cluster1_table.txt'
output_file_forward_primer_c2 = "Filtered_forward_primers_cluster2.txt"
output_file_reverse_primer_c2 = "Filtered_reverse_primers_cluster2.txt"
forward_list_c1 = []
reverse_list_c1 = []
forward_list_c2 = []
reverse_list_c2 = []
primer_min= 490
primer_max= 511
primer_pairs_c1= 'primer_pairs_cluster1.txt'
primer_pairs_c2= 'primer_pairs_cluster2.txt'

#####################################################
### make a list of the forward en reverse primers ###
#####################################################
with open (new_file_forward, 'r') as file:
    for line in file:
        if 'Primers' in line:
           print ('no')
        elif 'Sequence'in line:
           print('no')
        else:
            forward_list_c1 = forward_list_c1 + line.split()

with open (new_file_reverse, 'r') as file:
    for line in file:
        if 'Primers' in line:
           print ('no')
        elif 'Sequence'in line:
           print('no')
        else:
           reverse_list_c1 = reverse_list_c1 + line.split()

with open (output_file_forward_primer_c2, 'r') as file:
    for line in file:
        if 'Primers' in line:
           print ('no')
        elif 'Sequence'in line:
           print('no')
        else:
            forward_list_c2 = forward_list_c2 + line.split()

with open (output_file_reverse_primer_c2, 'r') as file:
    for line in file:
        if 'Primers' in line:
           print ('no')
        elif 'Sequence'in line:
           print('no')
        else:
           reverse_list_c2 = reverse_list_c2 + line.split()

#################################################
### filter on primer product and create pairs ###
#################################################
f1=open(primer_pairs_c1, 'w')
f1.write("Start \tSequence \t\tLength \tGC% \tTm \tany_th \tend_th \thpin \tquality  \n")
i=0
j=0
k=0
l=100

while k <30100:
    if j < len(reverse_list_c1):
        if i < len(forward_list_c1):
            if int(forward_list_c1[i]) > k and int(forward_list_c1[i]) < l:
                TMP = int(reverse_list_c1[j])-int(forward_list_c1[i])
                if TMP  > primer_min and TMP < primer_max:
                    print ('true')
                    f1.write(str(forward_list_c1[i])+'\t'+forward_list_c1[i+1]+'\t'+forward_list_c1[i+2]+'\t'+forward_list_c1[i+3]+'\t'+forward_list_c1[i+4]+'\t'+forward_list_c1[i+5]+'\t'+forward_list_c1[i+6]+'\t'+forward_list_c1[i+7]+'\t'+forward_list_c1[i+8]+'\n'+reverse_list_c1[j]+'\t'+reverse_list_c1[j+1]+'\t'+reverse_list_c1[j+2]+'\t'+reverse_list_c1[j+3]+'\t'+reverse_list_c1[j+4]+'\t'+reverse_list_c1[j+5]+'\t'+reverse_list_c1[j+6]+'\t'+reverse_list_c1[j+7]+'\t'+reverse_list_c1[j+8]+'\n'+'Product size: '+ str(int(reverse_list_c1[j])-int(forward_list_c1[i])+1)+'\n')
                    i = i + 9
                else:
                    i = i + 9
            else:
                i = i + 9
        else:
            i = 0
            j = j + 9
    else:
        i=0
        j=0
        k= k + 400
        l= l + 400

f1.close()

f2=open(primer_pairs_c2, 'w')
f2.write("Start \tSequence \t\tLength \tGC% \tTm \tany_th \tend_th \thpin \tquality  \n")

i=0
j=0
k=0
l=100

while k <30100:
    if j < len(reverse_list_c2):
        if i < len(forward_list_c2):
            if int(forward_list_c2[i]) > k and int(forward_list_c2[i]) < l:
                TMP = int(reverse_list_c2[j])-int(forward_list_c2[i])
                if TMP  > primer_min and TMP < primer_max:
                    print ('true')
                    f2.write(str(forward_list_c2[i])+'\t'+forward_list_c2[i+1]+'\t'+forward_list_c2[i+2]+'\t'+forward_list_c2[i+3]+'\t'+forward_list_c2[i+4]+'\t'+forward_list_c2[i+5]+'\t'+forward_list_c2[i+6]+'\t'+forward_list_c2[i+7]+'\t'+forward_list_c2[i+8]+'\n'+reverse_list_c2[j]+'\t'+reverse_list_c2[j+1]+'\t'+reverse_list_c2[j+2]+'\t'+reverse_list_c2[j+3]+'\t'+reverse_list_c2[j+4]+'\t'+reverse_list_c2[j+5]+'\t'+reverse_list_c2[j+6]+'\t'+reverse_list_c2[j+7]+'\t'+reverse_list_c2[j+8]+'\n'+'Product size: '+ str(int(reverse_list_c2[j])-int(forward_list_c2[i])+1)+'\n')
                    i = i + 9
                else:
                    i = i + 9
            else:
                i = i + 9
        else:
            i = 0
            j = j + 9
    else:
        i=0
        j=0
        k= k + 400
        l= l + 400

f2.close()

