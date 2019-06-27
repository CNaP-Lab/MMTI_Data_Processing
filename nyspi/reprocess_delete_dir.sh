######################################################
#
#             Devloped Sameera K. Abeykoon 
#             To delete old processed dir's and files
# 
#######################################################

echo Enter subject number
read sub_num

cd /mnt/hcp01/tnfcs_PI/${sub_num}

echo Remove unwanted folders Subject folder
rm -rf CTA_fMRI_* SOT_fMRI_* TL_fMRI_* RS_fMRI_*
rm -rf 2_RS_fMRI_* 2_TL_fMRI_* 2_SOT_fMRI_* 2_CTA_fMRI_*

cd /mnt/hcp01/tnfcs_PI/${sub_num}/MNINonLinear/Results

echo Remove unwanted folders inside MNINonLinear/Results
rm -rf CTA_fMRI_* SOT_fMRI_* TL_fMRI_* RS_fMRI_*
rm -rf 2_RS_fMRI_* 2_TL_fMRI_* 2_SOT_fMRI_* 2_CTA_fMRI_*
