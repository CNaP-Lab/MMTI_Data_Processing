# Developed by Sameera K. Abeykoon (March 08, 2019)
# This script will create 2_za folders inside unprocessed/3T

#echo Enter the Subject number  eg: 1491
#read sub_num
#echo "Subject No : ${sub_num}"

#echo Enter the Subject number list eg:0194 2264 2280
#read -a sub_list

sub_list=(50007 50008 50009)

#sub_list=(0194 2264 2450 2280 2812 2791 3012 2839)
echo ${sub_list[*]}

# Get the Subject number
# sub_num="${sub_path##*/}"

for sub_num in "${sub_list[@]}"; do :;
    # change to Subject folder
    sub_path="/mnt/hcp01/tnfcs_mini/"${sub_num}"/unprocessed/3T"
    cd ${sub_path}
    echo $PWD

    # get the fMRI data folders to an array
    fmri_array=($(find . -maxdepth 1 -type d -name "*fMRI*"))

    for i in "${fmri_array[@]}"; do :;
	j=${i##*/}
	echo ${j}
   
	# make directory 2_za files
	mkdir 2_za_${j}

	# copy the fMRI data folder to 2_za folder
	cp -R ${j}/* 2_za_${j} 
	cd 2_za_${j}
    
	# copy/move data 
	za_file=$(ls za*.nii.gz | sort -n | head -1)
	mv ${za_file} ${sub_num}_3T_2_za_${j}.nii.gz

	if ls *SBRef* 
	then
	    sb_file=$(ls *SBRef* | sort -n | head -1)
            echo ${sb_file}
            mv ${sb_file} ${sub_num}_3T_2_za_${j}_SBRef.nii.gz
	fi
   
	rm -rf z* *AVG* *.txt 

	cd ../
    done
done
