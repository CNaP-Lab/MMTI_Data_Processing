#!/bin/bash

# Developed by Sameera K. Abeykoon (June 1 2017)
# This script will change the orientation of fMRI_run_nu.nii.gz 

echo "Enter the final data directory inside hcp01/tnfcsi_PI ? " 
read sub_num
echo "You entered " $sub_num
#sub_num="3057_B0EPI0"
#data_dir="/mnt/hcp01/tnfcs_PI/3056_B0EPI5/unprocessed/3T"

cd /mnt/hcp01/tnfcs_PI/$sub_num/unprocessed/3T

# get the fMRI data folders to an array
fmri_array=($(find . -maxdepth 1 -type d -name "*fMRI*"))

# go inside each directory and remove the unwanted files and folders
for i in "${fmri_array[@]}"; do :;
     echo $i;
     cd $i
     echo $PWD
     
     #find . -type f -name "*${sub_num}_B0EPI0__*" | while read f; do mv $f $(echo $f | sed 's/${sub_num}_B0EPI0_/${sub_num}_/'); done	
     rename ${sub_num}_B0EPI0_ ${sub_num}_ ${sub_num}_B0EPI0_*
     cd ../
done

# get the fMRI data folders to an array
t2_array=($(find . -maxdepth 1 -type d -name "*T2w*"))

# get the fMRI data folders to an array
t1_array=($(find . -maxdepth 1 -type d -name "*T1w*"))


for i in "${t2_array[@]}"; do :;
     echo $i;
     cd $i
     echo $PWD  
     rename ${sub_num}_B0EPI0_ ${sub_num}_ ${sub_num}_B0EPI0_*
     cd ../
done

for i in "${t1_array[@]}"; do :;
     echo $i;
     cd $i
     echo $PWD

     # rename the sub_num
     rename ${sub_num}_B0EPI0_ ${sub_num}_ ${sub_num}_B0EPI0_*
     cd ../
done

cd FieldMap/
rename ${sub_num}_B0EPI0_ ${sub_num}_ ${sub_num}_B0EPI0_*
cd ../
