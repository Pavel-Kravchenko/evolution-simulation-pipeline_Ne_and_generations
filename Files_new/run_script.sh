echo "/Bash script srarted/"
mask=0.25

a=*.fasta
for x in $a
do
 echo "/Removing directory/"
 rm -R ${x%.fasta}"_"$mask
 echo "/Python script run/" 
 python "../alignment_reader_script.py" $x ${x%.fasta} $mask
 echo "/Done/"
 cd ${x%.fasta}"_"$mask
 pwd
 echo "/R script run/"
 Rscript "../../R_plot.R" --no-save --no-restore --args `pwd` $mask ${x%.fasta}
 echo "/Done/"
 echo "/Cleaning the derictory/"
 mv ../$x ./
 echo "/Done/"
 cd ..
done
echo "/Bash script ended successfully/"

