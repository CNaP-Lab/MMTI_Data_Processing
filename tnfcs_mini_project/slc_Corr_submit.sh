#########################################################################

#       to submit slcCorrFixFULL.m                                     #
# (/mnt/jxvs01/tools/matlab_path/Tipp_codes/Trunk/matlab_work)         #


########################################################################

echo Enter the Subject number list eg:0194 2264 2280
read -a sub_list

#sub_list=(0194 2264 2450 2280 2812 2791 3012 2839)
echo ${sub_list[*]}

#echo "MB factor ? "
#read MB
MB=6

cd /mnt/hcp01/codes/tnfcs_mini_project
echo "++++++++++++++++++++++++++++++++"
echo ${PWD}
 
for s_num in "${sub_list[@]}"; do :;

    # echo "Enter the subject number for XN data ? "
    echo ${s_num}
    echo ${MB}
    matlab -nodisplay -r "slc_Corr_list; quit"
    
done
#matlab -nodisplay -r "slc_Corr('${fmri_list[@]}','${MB}','${sub_path}'); quit"
#matlab -nodisplay -r "slc_Corr('${fmri_list[@]}','${MB}','${sub_path}'); quit"
