#!/bin/bash

# Developed by Sameera K. Abeykoon (January 2019)
# This a copy of dicm_to_nii.sh copy to HCP processed folder
# For VAT studies : and Creat VAT Freesufer files.

echo Enter the VAT study name example VAT_SCZ_1,VAT_SCZ_10_31 
read vat_name
echo "VAT name: ${vat_name}"

# make directory for HCP processed folder
#echo Enter the final HCP processed folder examples /mnt/hcp01/RDoC/50036
#read hcp_folder_path1
echo Enter the VAT_SCZ subject number example: 50087
read su_num

echo Is it vat_sud or vat_scz ?
read vat
hcp_folder_path1=/mnt/hcp01/pet_mri/${vat}/${su_num}

echo ${hcp_folder_path1}

sub_num=${hcp_folder_path1##*/}
hcp_folder_path=${hcp_folder_path1%/*}

echo "Subject No: ${sub_num}"
echo "HCP folder path: ${hcp_folder_path}"
echo Make HCP folder to process SCAN data
mkdir -p ${hcp_folder_path}/${sub_num}

echo Enter DICOM data directory with the path
read data_path
echo ${data_path}

current_path="$pwd"
cd /mnt/jxvs01/tools/matlab_path/dicm2nii
 
echo "change the directory to DICM2NII folder : {$PWD}"

# convert all the DICOM data to nifti format
echo Convert DICOM data to nifti
echo "--------------------------"
matlab -nodisplay -r "dicm2nii('$data_path', '${hcp_folder_path}/$sub_num', 0); quit"

# change to HCP data directory
cd ${hcp_folder_path}/${sub_num}
mkdir -p unprocessed
mkdir -p unprocessed/3T
mkdir -p unprocessed/3T/FieldMap

# remove the unwanted files and folders
echo remove the unwanted files and folders
echo "------------------------------------"
rm -rf *.json *.mat *.txt
rm -rf *.bvec *.bval
rm -rf *PET* Head_PD_ax* Head_striatum_press*
rm -rf hx_gre* rr_PRR* Head_hx_gre* 
rm -rf localizer* x3D_T1* x_rr*
rm -rf *hx_pCASL*
rm -rf Head_DTI_DSI_hybrid*
rm -rf Head_MPRAGE_CUBIT_1mm* Head_T2w_SPC_1mm*

echo "Current directory : ${pwd}"

# convert all the nifti files to nii.gz
echo Convert *.nii files to *.nii.gz
echo "-----------------------------"
matlab -nodisplay -r "gzip('*.nii'); quit"

# move SpinEchoFieldMap and EPI data to FieldMap data
spin=$(ls *SpinEchoFieldMap*.nii.gz)
mv ${spin} ${hcp_folder_path}/${sub_num}/unprocessed/3T/FieldMap
epi=$(ls *field_map*.nii.gz)
mv ${epi} ${hcp_folder_path}/${sub_num}/unprocessed/3T/FieldMap

# move T1w data after creating those folders
# t1w=$(ls *MPRAGE_CUBIT_p87mm*.nii)
t1w=($(find . -maxdepth 1 -type f -name "*MPRAGE_CUBIT_p87mm*.nii.gz"))

# t2w=$(ls *T2w_SPC_p87*.nii)
t2w=($(find . -maxdepth 1 -type f -name "*MPRAGE_CUBIT_p87mm*.nii.gz"))

# resting=$(ls *fMRI_Resting*.nii)
# rest_sb=$(ls *fMRI_Resting*SBRef.nii)
resting=($(find . -maxdepth 1 -type f -name "*fMRI_Resting*.nii.gz"))
rest_sb=($(find . -maxdepth 1 -type f -name "*fMRI_Resting*SBRef.nii.gz"))

# number of items in rest_SB array, t1w and t2w
sb_n=${#rest_sb[@]}
t1w_n=${#t1w[@]}
t2w_n=${#t2w[@]}

# move the resting state data to those folders
echo Move the resting state data *.nii.gz and *SBRef.nii.gz files
echo "-----------------------------------------------------------"
for ((i = 1 ; i <= ${sb_n} ; i++)); do  
    echo ${i};
    mkdir -p unprocessed/3T/RSPMR_fMRI_${i}
    mv *fMRI_Resting_${i}*SBRef.nii.gz unprocessed/3T/RSPMR_fMRI_${i}/${sub_num}_3T_RSPMR_fMRI_${i}_SBRef.nii.gz
    mv *fMRI_Resting_${i}*.nii.gz unprocessed/3T/RSPMR_fMRI_${i}/${sub_num}_3T_RSPMR_fMRI_${i}.nii.gz
done

rm -rf *.nii

# get T1w and T2w number of files then need to keep only normalized data
half_t2w=$(( ${t2w_n}/2 ))
half_t1w=$(( ${t1w_n}/2 ))

for ((j=1 ; j <= ${half_t2w} ; j++)); do
    # get the unnomarlized T2w data file 
    ny=$(ls *T2w_SPC_p87_${j}* | sort -n | head -1)
    # remove the unnormlized T2w data file
    rm -rf ${ny}
    mkdir -p unprocessed/3T/T2w_SPC${j}
    mv *T2w_SPC_p87_${j}*.nii.gz unprocessed/3T/T2w_SPC${j}/${sub_num}_3T_T2w_SPC${j}.nii.gz
done 

rm -rf *T2w_SPC_p87*.nii

for ((k=1 ; k <= ${half_t1w} ; k++)); do
    # get the unnomarlized T1w data file
    ny=$(ls *MPRAGE_CUBIT_p87mm_${k}*.nii.gz | sort -n | head -1)
    # remove the unnomarlized file
    rm -rf ${ny}
    mkdir -p unprocessed/3T/T1w_MPR${k}
    mv *MPRAGE_CUBIT_p87mm_${k}*.nii.gz unprocessed/3T/T1w_MPR${k}/${sub_num}_3T_T1w_MPR${k}.nii.gz
done   

rm -rf *MPRAGE_CUBIT_p87mm*.nii

# change into FieldMap folder 
echo FieldMap folder and rearrange those files
cd unprocessed/3T/FieldMap

# remove the EPI phase file
rm -rf *phase*
rm -rf *_SBRef.nii.gz

spin_ap=$(ls *SpinEchoFieldMap_AP*.nii.gz)
spin_pa=$(ls *SpinEchoFieldMap_PA*.nii.gz)
epi_f=$(ls *field_map*.nii.gz)

# SpinEchoFieldMap number files
s_ap_n=${#spin_ap[@]}
s_pa_n=${#spin_pa[@]}
epi_f_n=${#epi_f[@]}

for ((j=1 ; j <= ${s_ap_n} ; j++)); do
    mv *SpinEchoFieldMap_AP_${j}*.nii.gz ${sub_num}_3T_SpinEchoFieldMap_AP_${j}.nii.gz
done 

for ((j=1 ; j <= ${s_pa_n} ; j++)); do
    mv *SpinEchoFieldMap_PA_${j}*.nii.gz ${sub_num}_3T_SpinEchoFieldMap_PA_${j}.nii.gz
done 

for ((j=1 ; j <= ${s_pa_n} ; j++)); do
    mv *EPI_*${j}.nii.gz ${sub_num}_3T_GradientEchoFieldMap_${j}.nii.gz
done 

# change directory to HCP / Subject number folder
cd ${hcp_folder_path}/${sub_num}/unprocessed/3T
pwd 

# remove empty folders inside HCP /subject number folder
find . -type d -exec rmdir {} \;

# remove the remaining unwanted files
cd ${hcp_folder_path}/${sub_num}
rm -rf *.nii.gz

# change to dicm_to_nii codes folder
cd /mnt/hcp01/codes/dicm_to_nii

echo Create scanlog file
echo "---------------------------------------------"
python create_scanlog_vat.py ${data_path} ${vat_name}

echo sym links - fMRI and T1w and T2w data
echo "------------------------------------"
python scan_file_sym_links_all.py ${vat_name}_scanlog.txt ${hcp_folder_path1}

# move VAT_scanlog files to /mnt/jxvs01/pipelines/HCP/HCP_prep/SB_prep
mv VAT_*_scanlog.txt /mnt/jxvs01/pipelines/HCP/HCP_prep/SB_prep

# Create freesurfer files 
cd /mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples/Scripts/freesufer_volume_surface_scripts
sh Create_VAT_freesufer_scripts.sh ${hcp_folder_path1}

# Create volume processing files
cd /mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples/Scripts/templates/VolumeProcessingPipelineBatch_generator
ipython volume_SB_vat.py 

# change into freesufer folder to run those files
cd /mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples/Scripts

echo Freesufer files and VOLUMES file are ready to run
