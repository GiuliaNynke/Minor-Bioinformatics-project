#!/usr/bin/python3

##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

##################################
### variables, files and lists ###
##################################
# fetch fasta files
database = "nucleotide"
organism = "txid1335626[Organism]"
filter = "complete genome"
length = "27000:35000[Sequence length]"
outputname_fasta_file = "MERS_CoV.fasta"
# filter fasta files
outputname_filter_fasta_file = "MERS_CoV_filtered.fasta"
names = []
sequences = []
# create clusters
outputname_sumaclust = "MERS_CoV_clustered.fasta"
threshold_score = "0.97"
# separate clusters
outputname_cluster1 = "MERS_CoV_cluster1.fasta"
names_clustered = []
sequences_clustered = []
clusters =[]
# align sequences
outputname_muscle = "MERS_CoV_cluster1_aligned.fasta"
# prepare sequences for primer3
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
# create primers
primer3_core = "/mnt/StudentFiles/2019-20/NynkevEijk/project/primer3/primer3/src/primer3_core"
directory_c1 = "Cluster1"
directory_c2 = "Cluster2"
path_input_c1 = "/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script/MERS_CoV_cluster1_input_primer3.txt" #if you change variable inputname_primer3_cluster1 you have to change the name here
path_input_c2 = "/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script/MERS_CoV_cluster2_input_primer3.txt" #if you change variable inputname_primer3_cluster1 you have to change the name here
home= "/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script"
# filtering the primers
all_forward_primers_c1= "Primers_forward_cluster1.txt"
all_reverse_primers_c1= "Primers_reverse_cluster1.txt"
all_forward_primers_c2= "Primers_forward_cluster2.txt"
all_reverse_primers_c2= "Primers_reverse_cluster2.txt"
forward_primer_c1 = []
forward_primer_c2 = []
output_file_forward_primer_c1 = "Filtered_forward_primers_cluster1.txt"
output_file_forward_primer_c2 = "Filtered_forward_primers_cluster2.txt"
path_primers_cluster1 ='/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script/Cluster1'
path_primers_cluster2 ='/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script/Cluster2'
reverse_primer_c1 = []
reverse_primer_c2 = []
output_file_reverse_primer_c1 = "Filtered_reverse_primers_cluster1.txt"
output_file_reverse_primer_c2 = "Filtered_reverse_primers_cluster2.txt"
number_primers= '1000'
# remove double primers in cluster 1
temporary_list_forward = []
temporary_list_reverse = []
output_list_forward = []
output_list_reverse = []
output_file_forward = "forward_primers_cluster1_filtered.txt"
output_file_reverse= "reverse_primers_cluster1_filtered.txt"
# creating table of primers cluster 1
new_file_forward = 'forward_primers_cluster1_table.txt'
new_file_reverse = 'reverse_primers_cluster1_table.txt'
list_forward = []
list_reverse = []
# creating primer pairs
forward_list_c1 = []
reverse_list_c1 = []
forward_list_c2 = []
reverse_list_c2 = []
primer_min= 490
primer_max= 511
primer_pairs_c1= 'primer_pairs_cluster1.txt'
primer_pairs_c2= 'primer_pairs_cluster2.txt'


# 1.Fetch fasta file
########################
### fetch fasta file ###
########################
os.system("esearch -db %s -query '%s'|efilter -query '%s'|efilter -query '%s'|efetch -format fasta > %s"%(database,organism,filter,length,outputname_fasta_file))


# 2.Filter fasta file
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


# 3.Create clusters
#####################
### run sumaclust ###
#####################
os.system("sumaclust -t %s %s > %s"%(threshold_score,outputname_filter_fasta_file, outputname_sumaclust))


# 4. Separate clusters
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


# 5. Align sequences
##################
### run MUSCLE ###
##################
os.system("muscle -in %s -out %s -maxiters 2 -diags"%(outputname_cluster1 ,outputname_muscle))


# 6. prepare sequences for primer3
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


# 7. create primers
###################
### run primer3 ###
###################
os.mkdir(directory_c1)
os.chdir(directory_c1)
os.system("%s %s" %(primer3_core,path_input_c1))
os.chdir(home)

os.mkdir(directory_c2)
os.chdir(directory_c2)
os.system("%s %s" %(primer3_core,path_input_c2))
os.chdir(home)


# 8. filtering the primers
##########################################################
### Filtering and making a list of the forward primers ###
##########################################################
f1 = open(all_forward_primers_c1, 'w')

for filename in os.listdir(path_primers_cluster1):
    if filename.endswith(".for"):
        inputfile= open("{}/{}".format(path_primers_cluster1,filename),'r')
        for line in inputfile:
            if "ACCEPTABLE " in line:
                print("name")
            elif "#" in line:
                print ("name")
            else:
                f1.write(line)
f1.close()
inputfile.close()

f1 = open(output_file_forward_primer_c1, 'w')
file = open (all_forward_primers_c1, 'r')
text = file.readlines()
for lines in text:
    if lines[0:5] < number_primers:
        forward_primer_c1 = forward_primer_c1 + lines.split()
file.close()

print (forward_primer_c1)

f2 = open(all_forward_primers_c2, 'w')

for filename in os.listdir(path_primers_cluster2):
    if filename.endswith(".for"):
        inputfile= open("{}/{}".format(path_primers_cluster2,filename),'r')
        for line in inputfile:
            if "ACCEPTABLE " in line:
                print("name")
            elif "#" in line:
                print ("name")
            else:
                f2.write(line)
f2.close()
inputfile.close()

f2 = open(output_file_forward_primer_c2, 'w')
file = open (all_forward_primers_c2, 'r')
text = file.readlines()
for lines in text:
    if lines[0:5] < number_primers:
        forward_primer_c2 = forward_primer_c2 + lines.split()
file.close()

print (forward_primer_c2)

#####################################
### Filtering the forward primers ###
#####################################
ath=7
eth=8
hp=9
q=10
i=0

f1.write("Forward Primers \n")
f1.write("Start \tSequence \t\tLength \tGC% \tTm \tany_th \tend_th \thpin \tquality  \n")

while q < len(forward_primer_c1):
    if forward_primer_c1[q] < "1.00":
        print ("true")
        f1.write (str(forward_primer_c1[i+2]) + "\t"+ str(forward_primer_c1[i+1]) +"\t"+ str(forward_primer_c1[i+3])+"\t"+ str(forward_primer_c1[i+5])+ "\t"+ str(forward_primer_c1[i+6])+"\t"+ str(forward_primer_c1[i+7])+"\t"+ str(forward_primer_c1[i+8])+"\t"+ str(forward_primer_c1[i+9])+"\t"+ str(forward_primer_c1[i+10])+ "\n")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
    else:
        print ("false")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
f1.close()

ath=7
eth=8
hp=9
q=10
i=0

f2.write("Forward Primers \n")
f2.write("Start \tSequence \t\tLength \tGC% \tTm \tany_th \tend_th \thpin \tquality  \n")

while q < len(forward_primer_c2):
    if forward_primer_c2[q] < "1.00":
        print ("true")
        f2.write (str(forward_primer_c2[i+2]) + "\t"+ str(forward_primer_c2[i+1]) +"\t"+ str(forward_primer_c2[i+3])+"\t"+ str(forward_primer_c2[i+5])+ "\t"+ str(forward_primer_c2[i+6])+"\t"+ str(forward_primer_c2[i+7])+"\t"+ str(forward_primer_c2[i+8])+"\t"+ str(forward_primer_c2[i+9])+"\t"+ str(forward_primer_c2[i+10])+ "\n")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
    else:
        print ("false")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
f2.close()


##########################################################
### Filtering and making a list of the reverse primers ###
##########################################################
f1 = open(all_reverse_primers_c1, 'w')

for filename in os.listdir(path_primers_cluster1):
    if filename.endswith(".rev"):
        inputfile= open("{}/{}".format(path_primers_cluster1,filename),'r')
        for line in inputfile:
            if "ACCEPTABLE " in line:
                print("name")
            elif "#" in line:
                print ("name")
            else:
                f1.write(line)
f1.close()
inputfile.close()

f1 = open (output_file_reverse_primer_c1, 'w')
file = open (all_reverse_primers_c1, 'r')
text = file.readlines()
for lines in text:
    if lines[0:5] < number_primers:
        reverse_primer_c1 = reverse_primer_c1 + lines.split()
file.close()

print (reverse_primer_c1)

f2 = open(all_reverse_primers_c2, 'w')

for filename in os.listdir(path_primers_cluster2):
    if filename.endswith(".rev"):
        inputfile= open("{}/{}".format(path_primers_cluster2,filename),'r')
        for line in inputfile:
            if "ACCEPTABLE " in line:
                print("name")
            elif "#" in line:
                print ("name")
            else:
                f2.write(line)
f2.close()
inputfile.close()

f2 = open (output_file_reverse_primer_c2, 'w')
file = open (all_reverse_primers_c2, 'r')
text = file.readlines()
for lines in text:
    if lines[0:5] < number_primers:
        reverse_primer_c2 = reverse_primer_c2 + lines.split()
file.close()

print (reverse_primer_c2)

#####################################
### Filtering the reverse primers ###
#####################################
ath=7
eth=8
hp=9
q=10
i=0

f1.write("Reverse Primers \n")
f1.write("Start \tSequence \t\tLength \tGC% \tTm \tany_th \tend_th \thpin \tquality  \n")

while q < len(reverse_primer_c1):
    if reverse_primer_c1[q] < "1.00":
        print ("true")
        f1.write (str(reverse_primer_c1[i+2]) + "\t"+ str(reverse_primer_c1[i+1]) +"\t"+ str(reverse_primer_c1[i+3])+"\t"+ str(reverse_primer_c1[i+5])+ "\t"+ str(reverse_primer_c1[i+6])+"\t"+ str(reverse_primer_c1[i+7])+"\t"+str(reverse_primer_c1[i+8])+"\t"+ str(reverse_primer_c1[i+9])+"\t"+ str(reverse_primer_c1[i+10])+ "\n")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
    else:
        print ("false")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
f1.close()

ath=7
eth=8
hp=9
q=10
i=0

f2.write("Reverse Primers \n")
f2.write("Start \tSequence \t\tLength \tGC% \tTm \tany_th \tend_th \thpin \tquality  \n")

while q < len(reverse_primer_c2):
    if reverse_primer_c2[q] < "1.00":
        print ("true")
        f2.write (str(reverse_primer_c2[i+2]) + "\t"+ str(reverse_primer_c2[i+1]) +"\t"+ str(reverse_primer_c2[i+3])+"\t"+ str(reverse_primer_c2[i+5])+ "\t"+ str(reverse_primer_c2[i+6])+"\t"+ str(reverse_primer_c2[i+7])+"\t"+str(reverse_primer_c2[i+8])+"\t"+ str(reverse_primer_c2[i+9])+"\t"+ str(reverse_primer_c2[i+10])+ "\n")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
    else:
        print ("false")
        i = i + 11
        ath = ath + 11
        eth = eth + 11
        hp = hp + 11
        q = q + 11
f2.close()


# 9. remove double primers in cluster 1
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


# 10. creating table of primers cluster 1
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


# 11. creating primer pairs
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
