#!/bin/sh

# Developed by Sameera K. Abeykoon (June 21st 2018)

echo Enter the Subject number path eg: /mnt/hcp01/RDoC/50046
read sub_path
echo "Subject No path: ${sub_path}"
# change to the Subject directory
cd $sub_path

# get the fMRI data folders to an array
fmri_array=($(find . -maxdepth 1 -type d -name "*fMRI*"))

# go inside each directory and remove the unwanted files and folders
for i in "${fmri_array[@]}"; do :;
     echo $i;
     cd $i 
     echo $PWD
     #shopt -s extglob
     #rm -rf !*_nonlin_*
     find . -maxdepth 1 -type f \( \! -name '*nonlin_norm.nii.gz*' \) -exec rm {} \;
     find . -maxdepth 1 -type f \( -name '*SBRef_nonlin_norm.nii.gz*' \) -exec rm {} \;
     #find . -maxdepth 1 -type f \( \! -name '*nonlin*' \) -exec rm {} \;
     #find . -maxdepth 1 -type d \( \! -name '*nonlin*' \) -exec rm -rf {} \;
     cd ../
done
