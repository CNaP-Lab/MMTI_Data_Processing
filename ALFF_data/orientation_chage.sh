##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  clean pet images
#
###########################################################


echo Enter the final data folder
read niifolder

echo Change to source directory list data folders
cd ${niifolder}

st4=($(find . -maxdepth 1 -type d -name "*study4*"))

for j in "${st4[@]}"; do 
    i=$(basename ${j})
    echo ${i}
    cd ${niifolder}/${i}
    # locate *.nii.gz file	
    nii_file=($(find . -maxdepth 1 -type f -name "*.nii.gz*"))
    for k in "${nii_file[@]}"; do
	    k_base=$(basename ${k})
            echo ${k_base} orientation change 
            echo "------------------------------------------"
	    mri_convert --out_orientation RAS ${k_base} ${k_base}
     done
    
done
