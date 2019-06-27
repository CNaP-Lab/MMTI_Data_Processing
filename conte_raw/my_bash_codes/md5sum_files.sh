#!/bin/bash

# This will list out the md5sum details of the all the files in the dir
# and sub directories

# Enter the directory name
dir1=$1    
# Enter the outputfile name to save md5sum data  of files in dir and sub dir
textfile1=$2

echo $dir1>>$textfile1
echo "">>$textfile1

#md5sum dir1/* >>$textfile1

#for i in $dir1; do
# [[ -f "$i" ]] && md5sum "$i" >> $textfile1; 
#done

cd /$dir

find -type f -exec md5sum '{}' \; > $textfile1                    
