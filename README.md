# Minor-Bioinformatics-project
Made by Nynke van Eijk en Giulia Kleijwegt
Made in May 2020


# Installation Fetch FASTA files
sudo apt install ncbi-ebtrez-direct
# Use Fetch FASTA files
esearch -db nucleotide -query "txid1335626[Organism]"| efilter -query "complete genome"| efilter -query "27000:35000[Sequence length]| efetch -format fasta > mers_cov.fasta

# Installation SUMACLUST
wget https://git.metabarcoding.org/obitools/sumaclust/uploads/69f757c42f2cd45212c587e87c75a00f/sumaclust_v1.0.20.tar.gz  
tar -zxvf sumaclust_v1.0.20.tar.gz
cd sumaclust_v1.0.20
make
# Use SUMACLUST
sumaclust -t 0.97 input.fasta > output.fasta

# Installation MUSCLE
wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz 
tar -zxvf muscle3.8.31_i86linux64.tar.gz
mv muscle3.8.31_i86linux64 muscle
# Use MUSCLE
muscle -in input.fasta -out output.afa -maxiters 2 -diags

# Installation Primer 3
sudo apt-get install -y build-essential g++ cmake git-all
git clone https://github.com/primer3-org/primer3.git primer3
cd primer3/src
make
make test
# Use Primer 3
primer3_core input.afa


