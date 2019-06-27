#########################################################

#       to submit for TIPP

##########################################################

echo "Final hcp(/mnt/hcp01) subject directory ? "
read sub_dir

echo "QCplot folder  ? "
read qcplot_dir

#cd qcplot_dir

matlab -nodisplay -r "tipp_hcp_update('${sub_dir}','${qcplot_dir}'); quit" 2>"/mnt/hcp01/codes/outputs/tipp_outputs/Tipp_error.log" 1> "/mnt/hcp01/codes/outputs/tipp_outputs/Tipp_output.log"

# get the basename
base="$(basename ${qcplot_dir})"

if [ ${base}==rtms ]
then
     chgrp -R rtms qcplot_dir
     echo ${qcplot_dir} "rtms"
elif [ ${base}==vatsud_data ]
     chgrp -R vatsud qcplot_dir
     echo ${qcplot_dir} "vatsud"
elif [ ${base}==vatscz_data ]
     chgrp -R vatscz qcplot_dir
     echo ${qcplot_dir} "vatscz"
else
     echo "Not a correct folder"
fi
