#!/bin/bash

# Developed by Sameera K. Abeykoon (June 1 2017)
# This script will change the orientation of fMRI_run_nu.nii.gz 

echo "Enter the final data directory inside hcp01/tnfcsi_PI ? " 
read sub_num
echo "You entered " $sub_num
#sub_num="3057_B0EPI0"
#data_dir="/mnt/hcp01/tnfcs_PI/3056_B0EPI5/unprocessed/3T"

cd /mnt/hcp01/tnfcs_PI/$sub_num/unprocessed/3T

pattern="fMRI_"

for d in *"${pattern}"*;do
echo $PWD
cd /mnt/hcp01/tnfcs_PI/$sub_num/unprocessed/3T/$d
echo $PWD
if [ -e ${sub_num}_3T_${d}.nii.gz ]; then
  gunzip ${sub_num}_3T_${d}.nii.gz
fi
mri_convert --in_type nii --out_type nii --out_orientation RAS ${sub_num}_3T_${d}.nii ./${sub_num}_3T_${d}.nii.gz
rm -rf ${sub_num}_3T_${d}.nii
cd ..
done

