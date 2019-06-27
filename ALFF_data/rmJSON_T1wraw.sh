##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  To copy and convert PAR REC to nifti.gz
#
###########################################################

echo Enter the final data folder
read niifolder

echo Change to source directory list data folders
cd ${niifolder}

sp_d=($(find . -maxdepth 1 -type d -name "*SP*"))
sc_d=($(find . -maxdepth 1 -type d -name "*SC*"))

for i in "${sp_d[@]}"; do 
    echo ${i};
    j=$(basename ${i})
    cd ${niifolder}/${j}
    rm -rf *.json
done

for i in "${sc_d[@]}"; do
    echo ${i};
    j=$(basename ${i})
    cd ${niifolder}/${j}
    rm -rf *.json
done
