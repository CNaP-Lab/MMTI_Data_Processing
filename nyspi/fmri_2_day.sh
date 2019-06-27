#!/bin/bash

# Developed by Sameera K. Abeykoon (June 1 2017)
# This script will change the orientation of fMRI_run_nu.nii.gz 

echo "Enter the final data directory inside hcp01/tnfcsi_PI ? " 
read sub_num
echo "You entered " $sub_num
#sub_num="3057_B0EPI0"
#data_dir="/mnt/hcp01/tnfcs_PI/3056_B0EPI5/unprocessed/3T"

python physical_scanlog.py ${sub_num}
cd /mnt/hcp01/tnfcs_PI/$sub_num/unprocessed/3T

# Run the following python script to extract 
# the fMRI, T1w,T2w,fieldmap data from /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01
#source activate py35_nib
#python physical_scanlog.py
#source deactivate
 
# rename the 7123_ folders to 2_
find . -type d -name "*7123_*" | while read f; do mv $f $(echo $f | sed 's/7123_/2_/'); done

pattern="2_"

for d in *"${pattern}"*;do
    #echo $PWD
    cd /mnt/hcp01/tnfcs_PI/$sub_num/unprocessed/3T/$d
    echo $PWD

    # rename 7123_ files to 2_
    find . -type f -name "*7123_*" | while read f; do mv $f $(echo $f | sed 's/7123_/2_/'); done

    cd ..
done

