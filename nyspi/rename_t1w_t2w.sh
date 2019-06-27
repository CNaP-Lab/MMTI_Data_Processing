#!/bin/bash

# Developed by Sameera K. Abeykoon (June 1 2017)
# This script will change the orientation of fMRI_run_#no.nii.gz for
# the given subject folders 

echo "Enter the subject numbers inside hcp01/tnfcsi_PI ? " 
read -a sub_arr

# echo "You entered " $sub_arr
# sub_num="3057_B0EPI0"
# data_dir="/mnt/hcp01/tnfcs_PI/3056_B0EPI5/unprocessed/3T"

for sub_num in ${sub_arr[@]};do
        cd /mnt/hcp01/tnfcs_PI/${sub_num}/unprocessed/3T
        echo $PWD
	#data folders to an array
        t1w_array=($(find . -maxdepth 1 -type d -name "*T1w*"))
        t2w_array=($(find . -maxdepth 1 -type d -name "*T2w*"))
        
        k=1
        for t1 in ${t1w_array[@]};do
        	cd $t1
                echo $PWD
                file=${sub_num}3T_T1w_MPR${k}.nii.gz
                if [ -f "$file" ]
                then
                        mv file ${sub_num}_3T_T1w_MPR${k}.nii.gz
                fi

                let "k++"
                cd ../
        done
        l=1
        for t2 in ${t2w_array[@]};do
                cd $t2
                echo $PWD
                file=${sub_num}3T_T2w_MPR${l}.nii.gz
                if [ -f "$file" ]
                then
                	mv file ${sub_num}_3T_T2w_SPC${l}.nii.gz
                fi
                let "l++"
                cd ../
        done
done
