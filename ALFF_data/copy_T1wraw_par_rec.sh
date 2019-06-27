##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  To copy and convert PAR REC to nifti.gz
#
###########################################################

echo Enter the source folder
read src_data

echo Enter the final data folder
read niifolder

fmt=1
echo Final data format is ${fmt}

echo Change to source directory list data folders
cd ${src_data}

sp_d=($(find . -maxdepth 1 -type d -name "*SP*"))
sc_d=($(find . -maxdepth 1 -type d -name "*SC*"))

echo Change to DICM2NII folder to convert the data
cd /mnt/jxvs01/tools/matlab_path/dicm2nii

for i in "${sp_d[@]}"; do 
    echo ${i};
    mkdir -p ${niifolder}/${i}
    matlab -nodisplay -r "dicm2nii('${src_data}/${i}', '${niifolder}/${i}', ${fmt}); quit" 
done

for j in "${sc_d[@]}"; do
    echo ${j};
    mkdir -p ${niifolder}/${j}
    matlab -nodisplay -r "dicm2nii('${src_data}/${j}', '${niifolder}/${j}', ${fmt}); quit"
done
