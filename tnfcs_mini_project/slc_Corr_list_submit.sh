#########################################################################

#       to submit slcCorrFixFULL.m                                     #
# (/mnt/jxvs01/tools/matlab_path/Tipp_codes/Trunk/matlab_work)         #


########################################################################

#echo "MB factor ? "
#read MB
MB=6

cd /mnt/hcp01/codes/tnfcs_mini_project
echo "++++++++++++++++++++++++++++++++"
echo ${PWD}

matlab -nodisplay -r "slc_Corr_list; quit"
