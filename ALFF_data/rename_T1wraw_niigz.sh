##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  To copy and convert .nii to nifti.gz
#
###########################################################

echo Enter the final data folder
read niifolder

echo Change to niifolder
cd ${niifolder}

sp_d=($(find . -maxdepth 1 -type d -name "*SP*"))
sc_d=($(find . -maxdepth 1 -type d -name "*SC*"))

echo Convert the .nii file .nii.gz file

for i in "${sp_d[@]}"; do 
    echo ${i}
    cd ${niifolder}/${i}

    nii_file=$(ls *.nii | sort -n | head -1)

    matlab -nodisplay -r "gzip('*.nii'); quit" 
    rm -rf *.nii
done

for i in "${sc_d[@]}"; do 
    echo ${i}
    cd ${niifolder}/${i}
    
    nii_file=$(ls *.nii | sort -n | head -1)

    matlab -nodisplay -r "gzip('*.nii'); quit" 
    rm -rf *.nii
done
