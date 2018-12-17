# 
#    Developed by : Sameera Abeykoon
#
#    To run dcm2niix

echo " Enter the incoming dicom dir path ?"
read sub_path
echo "Subject No path: ${sub_path}"

echo " Enter the final last task data folder ?"
read final_data
final_path=/mnt/hcp01/pet_mri/vat_sud_task/${final_data}
echo "Final TASK data folder: ${final_path}"

# change to subject data dir
cd $sub_path

# get the task data folders to an array
#task_array=($(find . -maxdepth 1 -type d -name "*FMRI_TASK*"))

# get the task data folders without SBREF folders to an array
task_array=($(find . -maxdepth 1 -type d -name "*FMRI_TASK*" | grep -v SBREF))

# change to DICOMNIIX
cd /mnt/jxvs01/tools/mricrogl_lx

# convert multi echo DICOM to nifti data
for i in "${task_array[@]}"; do 
    echo ${i}
    #if [ ${i} == *"SBREF"* ]; then
    #	unset 'fmri_array["${fmri_array[$i]}"] fi
    ./dcm2niix -o ${final_path}/ -z y ${sub_path}/${i}
done
