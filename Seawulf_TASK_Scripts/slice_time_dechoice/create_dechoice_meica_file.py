"""
    Developed by Sameera K. Abeykoon (December 5th 2018)
    To extract slice timing infomation from .json files
    and save it a txt file

"""
from __future__ import print_function
import os, io
import numpy as np
import json
import sys
from six.moves import input
import glob

if len(sys.argv)<2:
    data_path = input("Enter the nifti files path ? ")
else:
    data_path = sys.argv[1]

# subject number
sub_num = os.path.basename(data_path)
print ("Subject number ", sub_num)

#file_ext = input("Enter the file extension for the .nii file ? ")
file_ext = "After_sl_"
data_dir = data_path + "/" + file_ext + "*"

# get T1w data file
#T1w_file = input("Enter the T1w file name ? ")
T1w_file = sub_num + "_T1w.nii"
if os.path.isfile(T1w_file):
    print (T1w_file)
else:
    T1w_file = input("Enter the T1w file name ? ")

# get the Prefix for file
Prefix = input("Enter the Prefix Insight ,MetaCog. Dechoice etc.. ")

# get the filename to save data
filename = data_path + "/" + sub_num + "_" + Prefix + "_meica.txt"

k = 1

# get the nifti files to process meica.py data    
res = [f for f in glob.glob(data_dir) if ".nii" in f and "e2" not in f and "e3" not in f]
with open(filename, 'a') as the_file:
    
    for name in sorted(res):
    	base1 = os.path.basename(name)
        base = os.path.splitext(base1)[0]
    	print (base)
    	the_file.write("meica.py -d \"" + base + ".nii" + ","+  base + "_e2.nii," +  base + "_e3.nii\"" + " -e 9.24,27.51,45.78 --daw=5 -b 15s " + T1w_file + " --MNI --prefix " +  Prefix + "_" + str(k) + "\n")
        k += 1
