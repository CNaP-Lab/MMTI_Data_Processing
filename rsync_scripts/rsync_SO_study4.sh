#  
# To rsync SO_study4_rawdata
# /nfsshare/export/c_of_Work/SO_study4_rawdata
# /mnt/jxvs02/conte_raw_data/SO_study4_rawdata

echo $PWD

rsync -rtvun /nfsshare/export/c_of_Work/SO_study4_rawdata/ /mnt/jxvs02/conte_raw_data/SO_study4_rawdata/ >> /mnt/hcp01/codes/outputs/jxvs02_work/SO_study4_rawdata.txt

#rsync -rtvu /nfsshare/export/c_of_Work/SO_study3_rawdata/ /mnt/jxvs02/conte_raw_data/SO_study3_rawdata/ >> /mnt/hcp01/codes/outputs/jxvs02_work/SO_study3_rawdata.txt
