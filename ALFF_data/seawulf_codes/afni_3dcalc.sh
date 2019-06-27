##########################################################
#
#  Developed by Sameera K. Abeykoon (January 2019)
#  To copy and convert PAR REC to nifti.gz
#
###########################################################

src_data="/gpfs/projects/VanSnellenbergGroup/PET_images"
#niifolder=$2

#echo Enter the final data folder
#read niifolder

echo Change to source directory list data folders
cd ${src_data}

st4=($(find . -maxdepth 1 -type d -name "*study4*"))

#echo Change to DICM2NII folder to convert the data
#cd /mnt/jxvs01/tools/matlab_path/dicm2nii

for j in "${st4[@]}"; do 
    i=$(basename ${j})
    echo ${i}
    cd ${src_data}/${i}
    rm -rf interp*
    hdr_file=$(ls *.hdr | sort -n )
    
    for k in ${hdr_file[@]}; do
        base="${k%.*}"
    	3dcalc -a ${k} -expr 'a' -prefix ${base}.nii
    done
    matlab -nodisplay -r "gzip('*.nii'); quit"
done
