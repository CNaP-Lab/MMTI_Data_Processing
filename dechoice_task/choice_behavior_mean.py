from __future__ import print_function
import numpy as np
import os, sys

# folder path 
path = "/mnt/jxvs01/incoming/PET_MRI/VAT_SUD/logfiles/"

# Provide the choice file .txt.txt file
scan_file1 = raw_input("Enter the .txt.txt file ? ")
scan_file = path + scan_file1

# enter the dtype of the reqiured categories colums
dtype1 = np.dtype([('RT','f8'), ('Category', '|S8'), ('Trial', 'f8'), ('Response', 'f8')])

# unpack the scanlog txt file
s_data = np.loadtxt(scan_file, skiprows=7, usecols=(2, 4, 5, 6), dtype=dtype1)

cat_s = []

# get the Category list
for j in (s_data):     
    cat_s.append(j[1])

# get unique category list
cat_u = np.unique(cat_s)

final_mean = []

for cat in cat_u:
     Trial_mean = []
     RT_mean = []
     R_mean = []
     for s in s_data:
         if s[1] == cat:
             RT_mean.append(s[0])
             Trial_mean.append(s[2])
             R_mean.append(s[3])
     final_mean.append((cat, np.nanmean(RT_mean), np.nanmean(Trial_mean), np.nanmean(R_mean)))

print (final_mean)

# save the mean values to a text file
topdir,tobedone = os.path.split(scan_file)

file_path = "/mnt/hcp01/pet_mri/vat_sud_task/Category_mean/Category_mean_"+ tobedone 

# save these details to the file
f = open(file_path, "w")

f.write("Category, RT_mean, Trail_mean, Response_mean \n")

# Take out the tuple brackets
f_mean =[', '.join(map(str, x)) for x in final_mean]

# save the values to a file
for i in f_mean:
    f.write(i+"\n")

f.close()
