#  
# To rsync LTM_backup/work to work folder inside /mnt/jxvs02/work
# First LTM_backup/work were transfered to nfshare/export folders
# work folder to /mnt/jxvs02/work

echo $PWD

rsync -rtvu /mnt/jxvs02/work/ /nfsshare/export/c_of_Work/LTM_backup/work/ >> /mnt/hcp01/codes/outputs/jxvs02_work/work_ltm_backup.txt
