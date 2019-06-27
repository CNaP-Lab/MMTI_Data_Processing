"""
This program will compare the files and directories in two directories.
"""

import os
import shutil

dir1 = "exampledir" # complete path to directory 1
dir2 = "exampledir2" # complete path to directory 2

#  all the files / directories in dir1 and list them 
files_1 = [file for file in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, file))]
files_2 = [file for file in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, file))]


for f_1 in files_1:
    # now check whether those files / directories are in the dir2 if not copy them
    if not f_1 in file_2:
	copy_file = dir1+"/"+f_1
        shutil.copy(copy_file, dir2)

