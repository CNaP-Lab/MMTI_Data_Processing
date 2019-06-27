# Developed by Sameera K. Abeykoon (March 08, 2019)

echo Enter the Subject number  eg: 1491
read sub_num
echo "Subject No : ${sub_num}"

# Get the Subject number
# sub_num="${sub_path##*/}"

# change to Subject folder
# if Subject dir not exists Create those folders
cd "/mnt/hcp01/tnfcs_mini/"
mkdir -p ${sub_num}
cd ${sub_num}
mkdir -p "unprocessed"
mkdir -p "unprocessed/3T"
new_path="/mnt/hcp01/tnfcs_mini/"${sub_num}"/unprocessed/3T"
cd "3T"
echo $PWD

# copy tnfcs subject unprocessed data to tnfcs_mini subject
cp -R /mnt/hcp01/tnfcs/"${sub_num}"/unprocessed/3T/* ${new_path}
# remove CTA* and TL* folders
rm -rf CTA* TL* THL* 2_*

# get the fMRI data folders to an array
fmri_array=($(find . -maxdepth 1 -type d -name "*fMRI*"))

for i in "${fmri_array[@]}"; do :;
    cd ${i}
    echo $PWD
    fmri_dir="${PWD##*/}"
    cd ../
done

cd "/mnt/hcp01/codes/tnfcs_mini_project"
# Create symlink for fMRI and T1w and T2w data for
# SpinEcho Fieldmaps
python tnfcs_mini_symlink.py ${sub_num}
