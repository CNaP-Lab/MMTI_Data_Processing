#!/bin/bash

# Developed by Sameera K. Abeykoon (November 2018)

#

echo Enter the Subject number path
read sub_path
echo "Subject No path: ${sub_path}"

echo Enter the Repetition Time seconds
read TR
echo "Repetition Time" ${TR}

python slice_time.py ${sub_path}

cd ${sub_path}
# get the slice timings files to an array
sl_time=($(find . -maxdepth 1 -type f -name "*.txt*"))

for i in "${sl_time[@]}"; do :;
    #echo ${i};
    k=($(basename ${i} .txt))
    echo "k" ${k}
    echo -TR ${TR}s -tzero 0 -tpattern ${sub_path}/${k}.txt -prefix After_sl_ ${k}.nii

done
