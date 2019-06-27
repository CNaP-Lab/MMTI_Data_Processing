#########################################################

#        Developed by Sameera Abeykoon                  #
#        to create FreesuferPipeline_Batch sh           #

##########################################################

if [ $# -eq 0 ]
  then
    echo "Enter the subject dirctory path example:/mnt/hcp01/RDoC/50070 ? "
    read sub_path
else
   sub_path=$1
fi

# get the basename for the subject dir
dir="${sub_path##*/}"
echo ${dir}

# get the dir name for the study and the study name
study="${sub_path%/*}"
echo ${study}# get the dir name for the study
study_path="${sub_path%/*}"
echo ${study_path}
study="${study_path##*/}"

# freesufer dir path
dir_path='/mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples/Scripts'

cp PreFreeSurferPipelineBatch_SB_VAT.sh ${dir_path}/PreFreeSurferPipelineBatch_SB_VAT_${dir}.sh
cp FreeSurferPipelineBatch_SB_VAT.sh ${dir_path}/FreeSurferPipelineBatch_SB_VAT_${dir}.sh
cp PostFreeSurferPipelineBatch_SB_VAT.sh ${dir_path}/PostFreeSurferPipelineBatch_SB_VAT_${dir}.sh

# change the dir to sciripts folder
cd ${dir_path}

replace "Datadir" "${study_path}" -- PreFreeSurferPipelineBatch_SB_VAT_${dir}.sh FreeSurferPipelineBatch_SB_VAT_${dir}.sh PostFreeSurferPipelineBatch_SB_VAT_${dir}.sh
replace "Final_subject" "${dir}" -- PreFreeSurferPipelineBatch_SB_VAT_${dir}.sh FreeSurferPipelineBatch_SB_VAT_${dir}.sh PostFreeSurferPipelineBatch_SB_VAT_${dir}.sh
