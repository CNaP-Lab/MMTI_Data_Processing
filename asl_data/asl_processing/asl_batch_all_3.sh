#!/bin/bash

# Developed by Sameera K. Abeykoon (March 19th 2018)

# This will run the ASL data processing for all 3 days data for the subjects

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

# cd to Cortical parcellation directory
cd /mnt/hcp01/scR21_asl/cortical_par/${sub_num}
echo $PWD
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++"

for i in {1..3}
do
 cd day_${i}/mri
 echo $PWD 
 rm -rf *.nii
 rm -rf *.nii.gz
 mri_convert --in_type mgz --out_type nii --out_orientation RAS T1.mgz ./T1.nii.gz
 mri_convert --in_type mgz --out_type nii --out_orientation RAS aseg.mgz ./aseg.nii.gz
 mri_convert --in_type mgz --out_type nii --out_orientation RAS aparc+aseg.mgz ./aparc_aseg.nii.gz

 # zip the T1 and aseg images and copy to asl data folders
 gunzip *.nii.gz

 echo T1.nii aseg.nii aparc_aseg.nii to /mnt/hcp01/scR21_asl/asl_results/${sub_num}/day_${i}/Anat folder
 echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
 echo "                                                                                        "
 
 cp T1.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i/Anat
 cp aseg.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i/Anat
 cp aparc_aseg.nii /mnt/hcp01/scR21_asl/asl_results/$sub_num/day_$i/Anat

 cd ../..
 echo $PWD
done

# change the directory to ASL folders
cd '/mnt/hcp01/scR21_asl/asl_results/ASLtbx'
echo $PWD
echo "++++++++++++++++++++++++++++++++++++++++++"

echo "ASL Data processing "
for i in {1..3};
#for i in 2 3
do
        echo $i
        echo " ASL data processing for ${sub_num}/day_$i "
        cp par_cp.m par.m
        replace "Subject_number" "${sub_num}/day_$i" -- par.m
	# matlab -nodisplay -r "batch_all('${sub_num}/day_${i}'); quit"
        matlab -nodisplay -r "batch_run; quit"
done

# Copy ASL CBF values to asl_results/ASL_CBF_values
echo Copy CBF values to /mnt/hcp01/scR21_asl/asl_results/ASL_CBF_values folder
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "                                                                        "
sh /mnt/hcp01/codes/asl_data/copy_rearrange_CBFData/copy_CBF_values.sh ${sub_num}

# change the folder /mnt/hcp01/scR21_asl/asl_results/ASL_CBF_values
cd /mnt/hcp01/scR21_asl/asl_results/ASL_CBF_values

# Then create one file for all three days using following python script
source activate py35
python /mnt/hcp01/codes/asl_data/copy_rearrange_CBFData/all_day3_labels.py ${sub_num}
