#!/bin/bash

# Developed by Sameera K. Abeykoon (March 19th 2018)

# This will run the ASL data processing for all 3 days data for the subjects

echo Enter the Subject number
read sub_num
echo "Subject No: ${sub_num}"

# change the directory to ASL folders
cd '/mnt/hcp01/scR21_asl/asl_results/ASLtbx'

echo "ASL Data processing "
#for i in {1..3};do
for i in 1 2
do
        echo $i
        echo " ASL data processing for ${sub_num}/day_$i "
        cp par_cp.m par.m
        replace "Subject_number" "${sub_num}/day_$i" -- par.m
	# matlab -nodisplay -r "batch_all('${sub_num}/day_${i}'); quit"
        matlab -nodisplay -r "batch_run; quit"
done
