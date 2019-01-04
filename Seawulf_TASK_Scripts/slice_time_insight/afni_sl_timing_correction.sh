#!/bin/bash

# Developed by Sameera K. Abeykoon (November 2018)

# To do the slice timing correction 

module load shared
module load gsl/2.4.0
module load afni/17.2.05
module load anaconda/2

echo Enter the Subject number path
read sub_path
echo "Subject No path: ${sub_path}"

echo Enter the Repetition Time seconds
read TR
echo "Repetition Time" ${TR}

# get the script directory
dir=$(pwd)

# create slice time txt files
python slice_time.py ${sub_path}

cd ${sub_path}
# get the slice timings files to an array
sl_time=($(find . -maxdepth 1 -type f -name "*.txt*"))

for i in "${sl_time[@]}"; do :;
    #echo ${i};
    k=($(basename ${i} .txt))
    echo "k" ${k}
    3dTshift -TR ${TR}s -tzero 0 -tpattern @${sub_path}/${k}.txt -prefix After_sl_${k}.nii ${k}.nii

done

# change directory - scripts folder
cd ${dir}

# create meica.py txt file
python create_meica_file.py ${sub_path}
