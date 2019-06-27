# Developed by Sameera K. Abeykoon (March 08, 2019)
# Rename the folders and files from SB data 
# to *za_RSFC* *RSFC_za* *za_SO* *SO_za*

echo Enter the Subject number  eg: 50002
read sub_num
echo "Subject No : ${sub_num}"

# Get the Subject number
# sub_num="${sub_path##*/}"

# change to Subject folder
fmri_path="/mnt/hcp01/tnfcs_mini/"${sub_num}
un_path="/mnt/hcp01/tnfcs_mini/"${sub_num}"/unprocessed/3T"
process_path="/mnt/hcp01/tnfcs_mini/"${sub_num}/MNINonLinear/Results
t1w_path="/mnt/hcp01/tnfcs_mini/"${sub_num}/T1w/Results

cd ${un_path}
echo $PWD
rename za_RSFC RSFC_za *za_RSFC*
rename za_SO SO_za *za_SO*

# get the fMRI data folders to an array
Unfmri_array=($(find . -maxdepth 1 -type d -name "*za*"))

for i in "${Unfmri_array[@]}"; do :;
    cd ${i}
    echo $PWD

    rename za_RSFC RSFC_za *za_RSFC*
    rename za_SO SO_za *za_SO*
    cd ../

done

cd ${fmri_path}
echo $PWD
# rename the folder names
rename za_RSFC RSFC_za *za_RSFC*
rename za_SO SO_za *za_SO*

# get the fMRI data folders to an array
fmri_array=($(find . -maxdepth 1 -type d -name "*za*"))

# Now reanme the files
for i in "${fmri_array[@]}"; do :;
    cd ${i}
    echo $PWD

    rename za_RSFC RSFC_za *za_RSFC*
    rename za_SO SO_za *za_SO*
    cd ../

done

cd ${process_path}
echo $PWD
rename za_RSFC RSFC_za *za_RSFC*
rename za_SO SO_za *za_SO*

# get the fMRI data folders to an array
mni_array=($(find . -maxdepth 1 -type d -name "*za*"))

for i in "${mni_array[@]}"; do :;
    cd ${i}
    echo $PWD

    rename za_RSFC RSFC_za *za_RSFC*
    rename za_SO SO_za *za_SO*
    cd ../

done

cd ${t1w_path}
echo $PWD
rename za_RSFC RSFC_za *za_RSFC*
rename za_SO SO_za *za_SO*

# get the fMRI data folders to an array
t1w_array=($(find . -maxdepth 1 -type d -name "*za*"))

for i in "${t1w_array[@]}"; do :;
    cd ${i}
    echo $PWD

    rename za_RSFC RSFC_za *za_RSFC*
    #rename RS_zaFC RSFC_za *RS_zaFC*
    rename za_SO SO_za *za_SO*
    cd ../

done


