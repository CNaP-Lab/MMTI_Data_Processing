#!/bin/sh

# Developed by Sameera K. Abeykoon (Nov 14th  2018)

echo Enter the Subject number path eg: /mnt/hcp01/RDoC/50046
read sub_path
#sub_path="/mnt/hcp01/test_folder/fmriprep_testing/500422"
echo "Subject No path: ${sub_path}"

cd ${sub_path}
mkdir anat func 

echo Enter the incoming dir path eg: /mnt/jxvs01/incoming/INSIGHT_Moeller/S3691_P7_SM
read data_path
#data_path="/mnt/jxvs01/incoming/Smoking_Cessation_Abi_Dargham/S3292_V40_AAD"
echo "data_path: ${data_path}"

# change to the dicm2iix 
cd /mnt/jxvs01/tools/mricrogl_lx

for i in "${data_path}"/*
do :;
     echo ${i}
     ./dcm2niix -z y -f %p_%s -o ${sub_path} ${i}
done
