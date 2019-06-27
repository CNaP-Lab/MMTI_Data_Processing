#!/bin/bash

#This will sore the md5sum data nto 2d array and compare details

# Enter the text file
t_file1=$1
t_file2=$2
# Enter the outputfile name to save comparision data
out_file=$3

echo $t_file1>>$out_file
echo "">>$out_file
echo $t_file2>>$out_file
echo"">>$out_file

no_lines_f1=$(wc -l $t_file1)
no_lines_f2=$(wc -l $t_file2)

no_col=2

declare -A matrix1
declare -A matrix2

for ((i=1;i<=no_lines_f1;i++)) do
    for ((j=1;j<=no_col;j++)) do 
      matrix1[$i,$j]=$(awk 'NR==row{print $col}' row=i col=j $t_file1)
      matrix2[$i,$j]=$(awk 'NR==row{print $col}' row=i col=j $t_file2)
   done
done

echo $(echo "${matrix1[@]}")
#echo $(echo "${matrix2[@]}")

