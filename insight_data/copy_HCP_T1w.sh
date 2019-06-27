#!/bin/bash

# Developed by Sameera K. Abeykoon (November 2018)

# This will T1w.nii.gz file from HCP processed folders

echo Enter the HCP folder path example:/mnt/hcp01/pet_mri/vat_sud
read hcp_path
echo "HCP folder path: ${hcp_path}"
 
echo Enter the TASK folder path example:/mnt/hcp01/pet_mri/vat_sud_task
read task_path
echo "TASK folder path: ${task_path}"

# provide subject numbers
read -p "Enter subject numbers separated by 'space' : " folders

# copy T1w.nii.gz file from the HCP folder to 
for i in ${folders[@]}
do
   echo ""
   echo "User entered value :"$i    # or do whatever with individual element of the array
   echo ""
   cp ${hcp_path}/${i}/T1w/T1w.nii.gz ${task_path}/${i}/${i}_T1w.nii.gz
done


