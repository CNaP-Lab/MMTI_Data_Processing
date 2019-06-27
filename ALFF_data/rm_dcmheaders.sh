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

for j in "${sp_d[@]}"; do 
    i=$(basename ${j})
    echo ${i}

    cd ${niifolder}/${i}
    rm -rf dcmHeaders.mat
done

for j in "${sc_d[@]}"; do 
    i=$(basename ${j})
    echo ${i}

    cd ${niifolder}/${i}
    rm -rf dcmHeaders.mat
done
