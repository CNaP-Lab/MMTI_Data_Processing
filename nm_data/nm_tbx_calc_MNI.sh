#!/bin/bash

# Developed by Sameera K. Abeykoon (December 11th 2018) and adapted by JJW Feb & Mar 2019

# This will run the Neuromelanin data processing and run batch_calc_NM_MNI.m and 
# compile_results_vmdata.m to compile_results

# If no subject numbers provided 
if [ "$#" -eq  "0" ]
   then
     echo Enter the Subject number
     read -a sub_num
     echo "Subject No: ${sub_num[@]}"
else
     # Get the subject numbers
     sub_num=$1
fi

# Change the directory to NM toolbox folder
cd '/mnt/hcp01/nm_data/NM_toolbox'
#cd '/nfsshare/export/jodi/misc/mmti_neuromelanin/analysis/NM_toolbox'

echo "NM Data processing "
for s_num in "${sub_num[@]}";
do
        echo "NM data processing for ${s_num} "
        cp par_cp.m par.m
        replace "Subject_number" "${s_num}" -- par.m
	# run the NM_toolbox
        # matlab -nodisplay -r "batch_run; quit"
        matlab -nodisplay -r "batch_calc_NM_MNI; quit"
        # matlab -nodisplay -r "batch_calc_NM_MNI_topslice; quit" # Jodi still working on
        # /nfsshare/export/jodi/misc/mmti_neuromelanin/analysis
done


