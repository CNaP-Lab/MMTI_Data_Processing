#!/bin/bash

# Developed by Sameera K. Abeykoon (June 1 2017)
# This script will change the orientation of fMRI_run_#no.nii.gz for
# the given subject folders for DANA data

echo "Enter the subject numbers inside hcp01/dana_nyspi ? " 
read -a sub_arr

# echo "You entered " $sub_arr
# sub_num="3057_B0EPI0"
# data_dir="/mnt/hcp01/tnfcs_PI/3056_B0EPI5/unprocessed/3T"

for sub_num in ${sub_arr[@]};do 

    cd /mnt/hcp01/dana_nyspi/$sub_num/unprocessed/3T

    pattern="fMRI_"

    for d in *"${pattern}"*;do
    echo $PWD
    cd /mnt/hcp01/dana_nyspi/$sub_num/unprocessed/3T/$d
    echo $PWD
    if [ -e ${sub_num}_3T_${d}.nii.gz ]; then
    	gunzip ${sub_num}_3T_${d}.nii.gz
    fi
    mri_convert --in_type nii --out_type nii --out_orientation RAS ${sub_num}_3T_${d}.nii ./${sub_num}_3T_${d}.nii.gz
    rm -rf ${sub_num}_3T_${d}.nii
    cd ..
    done
done

