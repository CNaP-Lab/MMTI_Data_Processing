##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  To copy and convert .nii to nifti.gz
#
###########################################################

echo Enter the final data folder
read niifolder

echo Changed to niifolder
cd ${niifolder}

sp_d=($(find . -maxdepth 1 -type d -name "*SP*"))
sc_d=($(find . -maxdepth 1 -type d -name "*SC*"))

echo Deface the T1w files
echo "--------------------"

for i in "${sp_d[@]}"; do 
    j=$(basename ${i})
    echo ${j}
    
    # convert the *.nii to *nii.gz file using matlab
    cd ${niifolder}/${j}
    nii=$(ls *.nii | sort -n | head -1)
    if [ -e *.nii ]; then
       matlab -nodisplay -r "gzip('*.nii'); quit"
       rm -rf *.nii
    fi
    #matlab -nodisplay -r "gzip('*.nii'); quit"
    
    # locate *.nii.gz file
    nii_file=$(ls *.nii.gz | sort -n | head -1)
    mri_convert --out_orientation RAS *.nii.gz ${nii_file}
    base="${nii_file%%.*}"

    # deface the T1w data
    cd /mnt/hcp01/test_folder/deface
    mri_deface ${niifolder}/${j}/${nii_file} talairach_mixed_with_skull.gca face.gca ${base}_defaced.nii.gz
    cp ${base}_defaced.nii.gz  ${niifolder}/${j}
    rm -rf ${niifolder}/${j}/${nii_file}
done

for i in "${sc_d[@]}"; do 
    j=$(basename ${i})
    echo ${j}

    # convert the *.nii to *nii.gz file using matlab
    cd ${niifolder}/${j}
    matlab -nodisplay -r "gzip('*.nii'); quit"
    rm -rf *.nii

    # locate *.nii.gz file
    cd ${niifolder}/${j}
    nii_file=$(ls *.nii.gz | sort -n | head -1)
    mri_convert --out_orientation RAS *.nii.gz ${nii_file}
    base="${nii_file%%.*}"
 
    # deface the T1w data
    cd /mnt/hcp01/test_folder/deface
    mri_deface ${niifolder}/${j}/${nii_file} talairach_mixed_with_skull.gca face.gca ${base}_defaced.nii.gz
    cp ${base}_defaced.nii.gz  ${niifolder}/${j}
    rm -rf ${niifolder}/${j}/${nii_file}
done
