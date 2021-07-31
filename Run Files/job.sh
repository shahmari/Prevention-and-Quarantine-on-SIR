#PBS -l nodes=1:ppn=1
#PBS -m abe
#PBS -M shahmari.acer@gmail.com
cd CQPM
./local <<< "${filename}"
