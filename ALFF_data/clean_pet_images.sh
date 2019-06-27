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
    rm -rf *.hdr *.img *.nii *.hdr.nii.gz
    
    deface=$(ls *defaced* | sort -n)
    if [ ! -e "$deface" ]; then

	# locate *.nii.gz file	
	nii_file=($(find . -maxdepth 1 -type f -name "*.nii.gz*"))
        for k in "${nii_file[@]}"; do
	    k_base=$(basename ${k})
            echo ${k_base} orientation change 
            echo "------------------------------------------"
	    mri_convert --out_orientation RAS ${k_base} ${k_base}
	done
        
        rotated=($(find . -maxdepth 1 -type f -name "*rotated*"))   
        
        for rot in "${rotated[@]}"; do
            rot_file=$(basename ${rot})
            
            echo ${rot_file}
            echo "----------------------------------"

	    # deface the T1w data
	    cd /mnt/hcp01/test_folder/deface
	    mri_deface ${niifolder}/${i}/${rot_file} talairach_mixed_with_skull.gca face.gca defaced_${rot_file}
	    cp defaced_${rot_file} ${niifolder}/${i}
	    rm -rf ${niifolder}/${i}/${rot_file}
        done
    fi
    
done
