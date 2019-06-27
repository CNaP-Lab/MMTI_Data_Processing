#  Sameera K. Abeykoon (June 1 2017)
# This script will change the orientation of fMRI_run_#no.nii.gz for
# the given subject folders 

echo "Enter the subject numbers inside hcp01/tnfcsi_PI ? " 
read -a sub_arr

# echo "You entered " $sub_arr
# sub_num="3057_B0EPI0"
# data_dir="/mnt/hcp01/tnfcs_PI/3056_B0EPI5/unprocessed/3T"

for sub_num in ${sub_arr[@]};do
        cd /mnt/hcp01/tnfcs_PI/${sub_num}/unprocessed/3T
        echo $PWD
        rm -rf *T1w*
        rm -rf *T2w*
done
