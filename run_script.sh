echo "/Bash script srarted/"

mask=0.25
home=`pwd`

rm Files
mkdir Files
cd ./Files

for species in  2 4 8 16 32 64 128 #256 512 #1024 2048 4096 8192
do
 for generation in 2 4 8 16 32 64 128 #256 512 1024 2048 4096 8192
 do
  for mutation in  1 2 4 #8 16 32 64
  do
   python "$home/simulation_script.py" $species $generation $mutation y
  done
 done
done

a=*.fasta
for x in $a
do
 echo "/Removing directory/"
 rm -R ${x%.fasta}"_"$mask
 echo "/Python script run/" 
 python "$home/alignment_reader_script.py" $x ${x%.fasta} $mask
 echo "/Done/"
 cd ${x%.fasta}"_"$mask
 pwd
 echo "/R script run/"
 Rscript "$home/R_plot.R" --no-save --no-restore --args `pwd` $mask ${x%.fasta}
 echo "/Done/"
 echo "/Cleaning the derictory/"
 mv ../$x ./
 echo "/Done/"
 cd ..
done
echo "/Python heatmap script run/"
python "$home/heatmap_df_maker.py"
echo "/Done/"
cd ..
tar -cvf archive.tar ./Files

echo "/Bash script ended successfully/"

