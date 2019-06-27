#!/bin/sh

# Developed by Sameera K. Abeykoon (Nov 14th  2018)
# Brain Imaging Data Structure (BIDS)
# Need to use dicm2nii GUI to convert DICOM to nifti
# open MATLAB then type dicm2nii it will open dicm2nii GUI
# This will create .nii.gz and .json files
# This script will move those .nifti.gz and .json data to folder 
# structure as presented in the BIDS-managed data
# http://bids.neuroimaging.io/

echo Enter the Subject number path eg: /mnt/hcp01/RDoC/50046
read sub_path
#sub_path="/mnt/hcp01/test_folder/fmriprep_t"$(dirname $file)"esting/5042"
echo "Subject No path: ${sub_path}"

sub_num="$(basename -- ${sub_path})"
echo "Subject number: ${sub_num}"
study_path="$(dirname ${sub_path})"
echo "Study path: ${study_path}"

cd ${study_path}
mkdir -p ${sub_num}

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

# change to following Subject number folder
cd ${sub_path}

# If following folders are not present inside the subject
# folder it will create anat func fmap folders
mkdir -p anat func fmap

# rename require files with subject number
rename SpinEchoFieldMap_ ${sub_num}_SpinEchoFieldMap_ SpinEchoFieldMap_*
rename field_ ${sub_num}_field_ field_*
rename T1w_ ${sub_num}_T1w_ T1w_*
rename T2w_ ${sub_num}_T2w_ T2w_*
rename fMRI_ ${sub_num}_fMRI_ fMRI_*

for i in "${sub_path}"/*
do :;
     # move T1w and T2w to anat folder
     if echo *${i}* | grep -q "T1w"; then
	 mv ${i} anat
     elif echo *${i}* | grep -q "T2w"; then
         mv ${i} anat
     # move fMRI runs the func folder
     elif echo *${i}* | grep -q "fMRI"; then
         mv ${i} func 
     # move fieldmaps to fmap folder
     elif echo *${i}* | grep -q "map"; then
         mv ${i} fmap
     elif echo *${i}* | grep -q "SpinEcho"; then
         mv ${i} fmap
     else
         echo ${i}
     fi
    
done

# A parallel implementation of gzip for modern
# change directory
cd /mnt/jxvs01/tools/pigz-2.4

./pigz ${sub_path}/anat/${sub_nub}_T1w_*
./pigz ${sub_path}/anat/${sub_nub}_T2w_*

./pigz ${sub_path}/func/${sub_nub}_*
./pigz ${sub_path}/fmap/${sub_nub}_*

rm -rf ${sub_path}/anat/*.json.gz 
rm -rf ${sub_path}/func/*.json.gz
rm -rf ${sub_path}/fmap/*.json.gz
