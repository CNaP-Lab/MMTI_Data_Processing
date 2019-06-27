#!/bin/bash

# Developed by Sameera K. Abeykoon (MArch 19th 2018)
# This a copy of dicm_to_nii.sh only

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

# make directory for test data
mkdir -n /mnt/hcp01/test_folder/dicm_test/$sub_num

echo Enter DICOM data directory with the path
read data_path
echo ${data_path}

current_path="$pwd"
cd /mnt/jxvs01/tools/matlab_path/dicm2nii
 
echo "change directory to DICM2NII folder : {$PWD}"

matlab -nodisplay -r "dicm2nii('$data_path', '/mnt/hcp01/test_folder/dicm_test/$sub_num', 0); quit"

# change to test directory
cd /mnt/hcp01/test_folder/dicm_test/${sub_num}

echo "Current driectory : ${pwd}"
# Remove unwanted folders  
#rm *Resting*
#rm *SpinEchoFieldMap*
#rm *field_map*

