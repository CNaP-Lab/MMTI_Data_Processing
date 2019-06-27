# Developed by Sameera K. Abeykoon (March 08, 2019)

echo Enter the Subject number  eg: 1491
read sub_num
echo "Subject No : ${sub_num}"

# Get the Subject number
# sub_num="${sub_path##*/}"

# change to Subject folder
new_path="/mnt/hcp01/tnfcs_mini/"${sub_num}"/unprocessed/3T"
cd ${new_path}
echo $PWD

cp -R /mnt/hcp01/tnfcs/"${sub_num}"/unprocessed/3T/ ${new_path}
# remove CTA* and TL* folders
rm -rf CTA* TL*

# get the fMRI data folders to an array
fmri_array=($(find . -maxdepth 1 -type d -name "*fMRI*"))

for i in "${fmri_array[@]}"; do :;
    cd ${i}
    echo $PWD
    fmri_dir="${PWD##*/}"
    #fmri_file=($(find . -maxdepth 1 -type f -name "*fMRI*"))
    fmri_file=${sub_num}_3T_${fmri_dir}.nii.gz
    echo ${fmri_file}
    rm -rf ${fmri_file}
    echo /mnt/hcp01/tnfcs_PI/processed_2018/${sub_num}/unprocessed/3T/${fmri_dir}/${fmri_file}
    cp /mnt/hcp01/tnfcs_PI/processed_2018/${sub_num}/unprocessed/3T/${fmri_dir}/${fmri_file} .
    cd ../
done
