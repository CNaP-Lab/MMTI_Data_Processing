#  
# To rsync LTM_backup/work to work folder inside /mnt/jxvs02/work/work
# First LTM_backup/work were transfered to nfshare/export folders
# Inside work folder to /mnt/hcp01/work

cd /mnt/hcp01/
echo $PWD

rsync -rtvu /mnt/hcp01/work/ /nfsshare/export/c_of_Work/LTM_backup/work/ >> /mnt/hcp01/codes/outputs/jxvs02_work/work_inside_ltm_backup.txt
