#!/bin/sh

# Developed by Sameera K. Abeykoon (June 21st  2018)

echo Enter the Subject path eg: /mnt/hcp01/RDoC
read sub_path
echo "Subject path: ${sub_path}"
# change to the Subject directory
cd $sub_path

for j in $(ls -d */); do :;
     # change to the Subject directroy
     echo ${j}
     cd $sub_path/${j}
     echo $PWD 
     echo " +++++++++++++++++++++++++++++++++++++++++++++++++++"
     

     # get the fMRI data folders to an array
     fmri_array=($(find . -maxdepth 1 -type d -name "*fMRI*"))

     # go inside each directory and remove the unwanted files and folders
     for i in "${fmri_array[@]}"; do :;
     	echo $i;
     	cd $i 
     	echo $PWD
     	#shopt -s extglob  # didn't work
     	#rm -rf !*_nonlin_* # didn't work
     
     	#find . -maxdepth 1 -type f \( \! -name '*nonlin*' \) -exec rm {} \;
     	#find . -maxdepth 1 -type d \( \! -name '*nonlin*' \) -exec rm -rf {} \;
     	find . -maxdepth 1 -type f \( \! -name '*nonlin_norm.nii.gz*' \) -exec rm {} \;
        find . -maxdepth 1 -type f \( -name '*SBRef_nonlin_norm.nii.gz*' \) -exec rm {} \;
     	find -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -R
     	cd ../
     done
     cd ../
     echo "=========================================================="
     echo "                                                          "
done
