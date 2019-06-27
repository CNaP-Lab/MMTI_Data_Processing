#! /bin/bash
# Developed by Sameera Abeykoon
# This script will copy data from jodi/ExampleData

#echo "Enter the folder names inside hackthon folder ? " 
#read -a sub_arr
sub_arr=(philip jake john sameera zu)

cd /mnt/jxvs02/hackathon/jodi

for sub_num in ${sub_arr[@]};do
    
    rsync -rtvu ExampleData/ /mnt/jxvs02/hackathon/${sub_num}/ExampleData/
done
