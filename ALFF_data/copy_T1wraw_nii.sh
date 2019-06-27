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

read -p "Enter T1w folder names separated by 'space' : " folders

for i in "${folders[@]}"; do 
    echo ${i};
    nii_file=$(ls *.nii | sort -n | head -1)
    cp ${src_data}/${i}/${nii_file} ${niifolder}/${i}
    cd ${niifolder}/${i}
    mv ${nii_file} CS4_${i}_SPGR_SENSE.nii
    matlab -nodisplay -r "gzip('*.nii'); quit" 
    rm -rf *.nii
done

