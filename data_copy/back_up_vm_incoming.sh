#  commands to use to back up VM incoming fMRI data to external drive

cd /media/sameera/Back_Up_Book_jvans/jvans_backup

rsync -rtvu sameera@psych-jvans1.uhmc.sunysb.edu:/mnt/jxvs01/incoming/ incoming/ 

