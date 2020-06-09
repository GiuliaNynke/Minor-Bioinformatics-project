##############
### import ###
##############
import os
import Bio
from Bio import SeqIO

#################
### variables ###
#################
all_forward_primers_c1= "Primers_forward_cluster1.txt"
all_reverse_primers_c1= "Primers_reverse_cluster1.txt"
all_forward_primers_c2= "Primers_forward_cluster2.txt"
all_reverse_primers_c2= "Primers_reverse_cluster2.txt"
path_primers_cluster1 ='/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script/Cluster1'
path_primers_cluster2 ='/mnt/StudentFiles/2019-20/NynkevEijk/project/bioinformatics_project_script/Cluster2'
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

