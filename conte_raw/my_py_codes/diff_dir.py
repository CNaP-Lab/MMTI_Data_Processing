import os
from __future__ import print_function

dir1 = "dir1 complete path"
dir2 = "dir2 complete path"

files_1 =  [ f for f in listdir(dir1) if isfile(join(dir1,f)) ]
files_2 =  [ f for f in listdir(dir2) if isfile(join(dir2,f)) ]

f1=open("/mnt/hcp01/codes/outputs/textfile1.txt", "w+")
f1.write("(set(files_1) - set(files_2))")
f1.close()

f2=open("/mnt/hcp01/codes/outputs/textfile2.txt", "w+")
f2.write("(set(files_2) - set(files_1))")
f2.close()


