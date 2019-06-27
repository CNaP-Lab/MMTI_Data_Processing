#!/bin/bash

# Developed by Sameera K. Abeykoon (November 2018)

# This will T1w.nii.gz file from HCP processed folders
# to Insight and Metacog folders

#echo Enter the Subject number for Insight and Metacog data
#read sub_num
hcp_path=/mnt/hcp01/Insight
echo "HCP folder path: ${hcp_path}"
 
insight_path=/mnt/hcp01/insight_task/Insight_task
metacog_path=/mnt/hcp01/insight_task/Metacog
echo "Metacog folder path: ${metacog_path}"
echo "Insight folder path: ${insight_path}"

# provide subject numbers
read -p "Enter subject numbers separated by 'space' : " folders

# copy T1w.nii.gz file from the HCP folder to 
for i in ${folders[@]}
do
   echo ""
   echo "User entered value :"$i    # or do whatever with individual element of the array
   echo ""
   cp ${hcp_path}/${i}/T1w/T1w.nii.gz ${insight_path}/${i}/${i}_T1w.nii.gz
   gzip -d ${insight_path}/${i}/${i}_T1w.nii.gz
   cp ${hcp_path}/${i}/T1w/T1w.nii.gz ${metacog_path}/${i}/${i}_T1w.nii.gz
   gzip -d ${metacog_path}/${i}/${i}_T1w.nii.gz
   
done


