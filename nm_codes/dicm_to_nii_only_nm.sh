#!/bin/bash

# Developed by Sameera K. Abeykoon (December 2018)
# To process Neuromelanin (NM) data from Insight project

echo Enter the Subject numbers
read -a sub_num
echo "Subject No: ${sub_num[@]}"

for s_num in "${sub_num[@]}"; do
    
    # make directory for nm data analysis
    mkdir /mnt/hcp01/nm_data/$s_num/
    
    echo Enter input DICOM data directory for ${s_num}
    read data1
    echo "input day data: ${data1}"
    
    # change to DICOM2Nii folder
    current_path="$pwd"
    cd /mnt/jxvs01/tools/matlab_path/dicm2nii
 
    echo "change directory to DICM2NII folder : {$PWD}"
    
    matlab -nodisplay -r "dicm2nii('/mnt/jxvs01/incoming/INSIGHT_Moeller/${data1}', '/mnt/hcp01/nm_data/${s_num}', 0); quit"

    # change to nm directory
    cd  /mnt/hcp01/nm_data/$s_num/

    echo "Current driectory : ${pwd}"
    
    # Remove unwanted folders 
    rm *Resting*
    rm *SpinEchoFieldMap*
    rm *field_map*
    rm *Metacog*
    rm *Insight*

    # make Anat and NM folders for the data analysis
    mkdir Anat NM NM_norm
    if [ -e T1w_MPR_s003.nii ]
    then
           mv T1w_MPR_s003.nii Anat/
    elif [ -e T1w_MPR_norm.nii ]
    then
           mv T1w_MPR_norm.nii Anat/
    elif [ -e T1w_MPR_norm.nii ]
    then
           mv T1w_MPR_1_s003.nii Anat/
    else
           echo " Missing T1w_MPR_norm.nii or T1w_MPR_s003.nii data or T1w_MPR_1_s003.nii"
    fi

    # move the NM data files to those folders
    NM_file=$(ls hx_gre_*.nii | sort -n | head -1)
    mv ${NM_file} NM/
    
    # move the NM data files to those folders
    NM_norm_file=$(ls hx_gre_*.nii)
    mv ${NM_norm_file} NM_norm/
    
    # move nm_data codes directory
    cd /mnt/hcp01/codes/nm_data
done 

# Run the Neuromelanin Toolbox
#sh nm_tbx.sh ${sub_num[@]}

read -r -p "Are You Sure(continue to run NM toolbox)? [Y/n] " input
 
case $input in
    [yY][eE][sS]|[yY])
 echo "Yes"
 ;;
    [nN][oO]|[nN])
 echo "No"
       ;;
    *)
 echo "Invalid input..."
 exit 1
 ;;
esac

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
