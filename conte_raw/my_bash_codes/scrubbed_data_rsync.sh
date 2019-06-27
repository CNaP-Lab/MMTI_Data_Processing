# Developed by Sameera K. Abeykoon (March 08, 2019)
# This script will rsync data in following two folders
# 1 )/mnt/jxvs02/conte_processed_data/connectivity_default
# 2 )/mnt/jxvs02/conte_processed_data/connectivity_interleaved
# with /mnt/hcp01/old_data/scrubbed_datasets

inter_dir="/mnt/jxvs02/conte_processed_data/connectivity_interleaved"
default_dir="/mnt/jxvs02/conte_processed_data/connectivity_default"

# Check the data in default folder
echo ${default_dir}

cd ${default_dir}

# get the fMRI data folders to an array
s3_folder=($(find . -maxdepth 1 -type d -name "*study3*"))
s4_folder=($(find . -maxdepth 1 -type d -name "*study4*"))
s5_folder=($(find . -maxdepth 1 -type d -name "*study5*"))
s_folder=($(find . -maxdepth 1 -type d -name "study*"))

for i in "${s3_folder[@]}"; do :;
    j=${i##*/}
    echo ${j}
    echo /mnt/hcp01/old_data/scrubbed_datasets/${j}
    rsync -rtvu /mnt/hcp01/old_data/scrubbed_datasets/${j}/ ${j}/

done

for a in "${s4_folder[@]}"; do :;
    b=${a##*/}
    echo ${b}
    echo /mnt/hcp01/old_data/scrubbed_datasets/${b}
    rsync -rtvu /mnt/hcp01/old_data/scrubbed_datasets/${b}/ ${b}/
done

for m in "${s5_folder[@]}"; do :;
    n=${m##*/}
    echo ${n}
    echo /mnt/hcp01/old_data/scrubbed_datasets/${n}
    rsync -rtvu /mnt/hcp01/old_data/scrubbed_datasets/${n}/ ${n}/
done

# Check the data -  interleaved folder
echo ${inter_dir}

cd ${inter_dir}

# get the fMRI data folders to an array
s3_dir=($(find . -maxdepth 1 -type d -name "*study3*"))
s4_dir=($(find . -maxdepth 1 -type d -name "*study4*"))
s5_dir=($(find . -maxdepth 1 -type d -name "*study5*"))
s_dir=($(find . -maxdepth 1 -type d -name "study*"))

for i in "${s3_dir[@]}"; do :;
    j=${i##*/}
    echo ${j}
    echo /mnt/hcp01/old_data/scrubbed_datasets/${j}
    rsync -rtvu /mnt/hcp01/old_data/scrubbed_datasets/${j}/ ${j}/

done

for a in "${s4_dir[@]}"; do :;
    b=${a##*/}
    echo ${b}
    echo /mnt/hcp01/old_data/scrubbed_datasets/${b}
    rsync -rtvu /mnt/hcp01/old_data/scrubbed_datasets/${b}/ ${b}/

done

for m in "${s5_dir[@]}"; do :;
    n=${m##*/}
    echo ${n}
    echo /mnt/hcp01/old_data/scrubbed_datasets/${n}
    rsync -rtvu /mnt/hcp01/old_data/scrubbed_datasets/${n}/ ${n}/

done
    
# Merge two lists
#sort "${s_folder[@]}" "${s4_dir[@]}" > s_list
echo "++++++++++++++++++++++++++++++++++++++++++++++++"
echo "                                                "
cd /mnt/hcp01/old_data/scrubbed_datasets 

scrub_dir=($(find . -maxdepth 1 -type d -name "study*"))

for m in "${scrub_dir[@]}"; do :;
    #echo ${m}
    n=${m##*/}
    echo ${n}
    echo ${PWD}
    if [[ "${s_folder[@]}" == *" ${m} "* ]] ; then
        echo "OK"
        #rm -rf ${n}
	#echo ${m} "exists default"
    elif [[ "${s_dir[@]}" == *" ${m} "* ]]; then
        #echo ${m} "exists inter"
        echo "OK"
	#rm -rf ${n}
    else
	echo ${m} "missing"
    fi
    echo "++++++++++++++++++++++++++++++"
done
	
    


