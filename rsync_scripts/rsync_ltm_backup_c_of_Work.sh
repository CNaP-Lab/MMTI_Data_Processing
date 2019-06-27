#  
# To rsync LTM_backup/work to copies_of_work/work
# First they were transfered to nfshare/export folders

cd /nfsshare/export/c_of_Work
echo $PWD

rsync -rtvu work/ /nfsshare/export/c_of_Work/LTM_backup/work/ >> /mnt/hcp01/codes/outputs/jxvs02_work/ltm_backup_work.txt
