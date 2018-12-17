#!/bin/bash

# Developed by Sameera K. Abeykoon (November 2018)

# This will convert Metacog and Insight multiecho DICOM data to 
# nifti and json files. One DICOM file wwill crteat three nifts files
# three json files for all three echos

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

cd '/mnt/hcp01/insight_task'
mkdir -p ${sub_num}

cd '/mnt/hcp01/insight_task/Insight_task'
mkdir -p ${sub_num}

cd '/mnt/hcp01/insight_task/Metacog'
mkdir -p ${sub_num}

insight_folder='/mnt/hcp01/insight_task/Insight_task/'${sub_num}
metacog_folder='/mnt/hcp01/insight_task/Metacog/'${sub_num}

echo Enter the Incoming data directory
read in_dir
echo "Incoming data dir: ${in_dir}"

# provide Inisght and Metacog folder names
read -p "Enter Insight and Metacog folder names separated by 'space' : " folders

# change directory to DICM2NIIX
cd '/mnt/jxvs01/tools/mricrogl_lx'

# convert the Insight and Metacog DICOM files to nifti and json files 
for i in ${folders[@]}
do
   echo ""
   echo "User entered value :"$i    # or do whatever with individual element of the array
   echo ""
   ./dcm2niix %p_%s -o /mnt/hcp01/insight_task/${sub_num} -z y ${in_dir}/${i}
done

# move the nifti files to Metacog and Insight folders
cd '/mnt/hcp01/insight_task/'${sub_num}

# rename the fMRI and T1w data to have the Subject number
rename fMRI_ ${sub_num}_fMRI_ fMRI_*
rename T1w_ ${sub_num}_T1w_ T1w_*

# move the fMRI and T1w dat to MetCog and Insight folder
mv *Insight* ${insight_folder}
mv *Metacog* ${metacog_folder}

cp *T1w* ${insight_folder}
cp *T1w* ${metacog_folder}

# remove the temporary folder
cd ../
rm -rf ${sub_num} 

