##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  To copy and convert PAR REC to nifti.gz
#
###########################################################

echo Enter the source folder
read src_data

#echo Enter the final data folder
#read niifolder

echo Change to source directory list data folders
cd ${src_data}

st4=($(find . -maxdepth 1 -type d -name "*study4*"))

#echo Change to DICM2NII folder to convert the data
#cd /mnt/jxvs01/tools/matlab_path/dicm2nii

for j in "${st4[@]}"; do 
    i=$(basename ${j})
    echo ${i}
    cd ${src_data}/${i}
    rm -rf interp*
    #matlab -nodisplay -r "dicm2nii('${src_data}/${i}', '${niifolder}/${i}', ${fmt}); quit" 
done
