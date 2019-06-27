#  
# To rsync SO_study2_rawdata
# /nfsshare/export/c_of_Work/SO_study2_rawdata
# /mnt/jxvs02/conte_raw_data/SO_study2_rawdata

echo $PWD

rsync -rtvu /nfsshare/export/c_of_Work/SO_study2_rawdata/ /mnt/jxvs02/conte_raw_data/SO_study2_rawdata/ >> /mnt/hcp01/codes/outputs/jxvs02_work/SO_study2_rawdata.txt

rsync -rtvu /nfsshare/export/c_of_Work/SO_study2_rawdata/ /mnt/jxvs02/conte_raw_data/SO_study2_rawdata/ >> /mnt/hcp01/codes/outputs/jxvs02_work/SO_study2_rawdata.txt
