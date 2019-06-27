#!/bin/bash
# This will list out the size of the files and directories recursively
# du displays "disk usage"
# h is for "human readable" (both, in sort and in du)
#max-depth=0 means du will not show sizes of subfolders 
#(remove that if you want to show all sizes of every file in every sub-, subsub-, ..., folder)

# Enter the directory name
dir1=$1    
# Enter the outputfile name to save the sizes of files and dir
textfile1=$2

echo $dir1>>$textfile1
echo "">>$textfile1

du -a -h --max-depth=5 |sort -n >>$textfile1

~                    
