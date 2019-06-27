#!/bin/bash

# Developed by Sameera K. Abeykoon (November 2018)

# This will convert vat_sud_task multiecho DICOM data to 
# nifti and json files. One DICOM file wwill creat 3 nifts
# files and 3 json files for all three echos

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

cd '/mnt/hcp01/pet_mri/vat_sud_task'
mkdir -p ${sub_num}

vat_task_folder='/mnt/hcp01/pet_mri/vat_sud_task/'${sub_num}

echo Enter the Incoming data directory
read in_dir
echo "Incoming data dir: ${in_dir}"
cd ${in_dir}

# provide VAT SUD TASK folder names
#read -p "Enter VAT SUD TASK folder names separated by 'space' : " folders
# get the fMRI TASK data folders to an array
fmri_array=($(find . -maxdepth 1 -type d -name "*HEAD_FMRI_TASK_*"))
declare -a folders=( ${fmri_array[@]/*SBREF*/} )

# change directory to DICM2NIIX
cd '/mnt/jxvs01/tools/mricrogl_lx'

# convert the VAT SUD TASK DICOM files to nifti and json files 
for i in ${folders[@]}
do
   echo ""
   echo "User entered value :"$i    # or do whatever with individual element of the array
   echo ""
   ./dcm2niix %p_%s -o /mnt/hcp01/pet_mri/vat_sud_task/${sub_num} -z y ${in_dir}/${i}
done

# rename VAT SUD TASK folders
cd ${vat_task_folder}

# rename the fMRI and T1w data to have the Subject number
rename Head_fMRI_ ${sub_num}_Head_fMRI_ Head_fMRI_*
#rename T1w_ ${sub_num}_T1w_ T1w_*

