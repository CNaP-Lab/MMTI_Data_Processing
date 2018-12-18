#!/bin/bash

# Developed by Sameera K. Abeykoon (MArch 19th 2018)

echo Enter the Subject numbers
read -a sub_num
echo "Subject No: ${sub_num[@]}"

for s_num in "${sub_num[@]}"; do
    
    # make directory for asl data analysis
    mkdir /mnt/hcp01/nm_data/$s_num/
    
    echo Enter input DICOM data directory for ${s_num}
    read data1
    echo "input day data: ${data1}"
    
    # change to DICOM2Nii folder
    current_path="$pwd"
    cd /mnt/jxvs01/tools/matlab_path/dicm2nii
 
    echo "change directory to DICM2NII folder : {$PWD}"
    
    /mnt/jxvs01/pipelines/HCP/usr/local/MATLAB/R2016b/bin/matlab -nodisplay -r "dicm2nii('/mnt/jxvs01/incoming/INSIGHT_Moeller/${data1}', '/mnt/hcp01/nm_data/${s_num}', 0); quit"

    # change to nm directory
    cd  /mnt/hcp01/nm_data/$s_num/

    echo "Current driectory : ${pwd}"
    
    # Remove unwanted folders 
    rm *Resting*
    rm *SpinEchoFieldMap*
    rm *field_map*
    rm *Metacog*
    rm *Insight*

    # make Anat ASL and REF folders for the data analysis
    mkdir Anat NM
    # copy the T1W_MPR_003.nii into cortical parcellation dir
    if [ -e T1w_MPR_s003.nii ]
    then
           #cp T1w_MPR_s003.nii /mnt/hcp01/scR21_asl/cortical_par/$sub_num/day_$i.nii
           mv T1w_MPR_s003.nii Anat/
    elif [ -e T1w_MPR_norm.nii ]
    then
           #cp T1w_MPR_norm.nii /mnt/hcp01/scR21_asl/cortical_par/$sub_num/day_$i.nii
           mv T1w_MPR_norm.nii Anat/
    else
           echo " Missing T1w_MPR_norm.nii or T1w_MPR_s003.nii data"
    fi

    # move the NM data files to those folders
    NM_file=$(ls hx_gre_* | sort -n | head -1)
    mv ${NM_file} NM/
    
    # move nm_data codes directory
    cd /mnt/hcp01/codes/nm_data
done 

# Run the Neuromelanin Toolbox
#sh nm_tbx.sh ${sub_num[@]}

# change the directory to NM folders
cd '/mnt/hcp01/nm_data/NM_toolbox'

echo "NM Data processing "
for s_num in "${sub_num[@]}";
do
        echo "NM data processing for ${s_num} "
        cp par_cp.m par.m
        replace "Subject_number" "${s_num}" -- par.m
        # run the NM_toolbox
        matlab -nodisplay -r "batch_run; quit"
done
