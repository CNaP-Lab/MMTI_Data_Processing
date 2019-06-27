#!/bin/sh

# Developed by Sameera K. Abeykoon (June 21st  2018)

echo Enter the Subject path eg: /mnt/hcp01/RDoC
read sub_path
echo "Subject path: ${sub_path}"
# change to the Subject directory
cd $sub_path

for j in $(ls -d */); do :;
     # change to the Subject directroy
     echo ${j}
     cd $sub_path/${j}
     echo $PWD
     
     rsync -rtvu sabeykoon@login.seawulf.stonybrook.edu:/gpfs/scratch/sabeykoon/HCP_data/nyspi/${j}/ .

done
