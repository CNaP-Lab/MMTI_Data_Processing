########################################################################

#       to submit for TIPP                                             #

########################################################################

#echo "Final hcp(example: /mnt/hcp01/RDoC) HCP processed directory ? "
#read sub_dir
sub_dir="/mnt/hcp01/RDoC"

#echo "QCplot folder  example: /mnt/jxvs01/imaging_data/rdoc ? "
#read qcplot_dir
qcplot_dir="/mnt/jxvs01/imaging_data/rdoc"

#cd qcplot_dir

# get the basename
base="$(basename ${qcplot_dir})"
echo ${base}


matlab -nodisplay -r "tipp_hcp('${sub_dir}','${qcplot_dir}'); quit" 2>"/mnt/hcp01/codes/outputs/tipp_outputs/${base}_Tipp_error.log" 1> "/mnt/hcp01/codes/outputs/tipp_outputs/${base}_Tipp_output.log"

# get the basename
base="$(basename ${qcplot_dir})"
echo ${base}

if [ ${base} = "rtms" ]
then
     chgrp -R rtms ${qcplot_dir}
     echo ${qcplot_dir} "rtms"
elif [ ${base} = "vatsud" ]
then
     chgrp -R vatsud ${qcplot_dir}
     echo ${qcplot_dir} "vatsud"
elif [ ${base} = "vatscz" ]
then
     chgrp -R vatscz ${qcplot_dir}
     echo ${qcplot_dir} "vatscz"
elif [ ${base} = "rdoc" ]
then
     chgrp -R rdoc ${qcplot_dir}
     echo ${qcplot_dir} "rdoc"
elif [ ${base} = "insight" ]
then
     chgrp -R insight ${qcplot_dir}
     echo ${qcplot_dir} "insight"
else
     echo "Not a correct folder"
fi

echo "                                    "
echo "++++++++++++++++++++++++++++++++++++"
echo "Finished processing without an error"
echo ${qcplot_dir}
echo "++++++++++++++++++++++++++++++++++++"
echo "                                    "
echo "                                    "
