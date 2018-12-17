from __future__ import print_function
import numpy as np
import os, sys

"""
	This script will find the mean values of the Choice category mean values from
        the .txt.txt files
"""

# folder path 
path = "/mnt/jxvs01/incoming/PETMR_VAT_Moeller/logfiles/"

# change directory 
os.chdir(path)
print (os.getcwd())

# Provide the subject number
sub_nu = raw_input("Enter the subject number ? ")

file_path = "/mnt/hcp01/pet_mri/vat_sud_task/Category_mean/Choice_Category_mean_"+ sub_nu + ".csv" 

# save these details to the file
f = open(file_path, "w")

f.write(sub_nu + "\n")
f.write(" \n")

# enter the dtype of the reqiured categories colums
dtype1 = np.dtype([('RT','f8'), ('Category', '|S8'), ('Trial', 'f8'), ('Response', 'f8')])

# get the choice .txt.txt files to a list
txt_list = []
for txt_file in np.sort(os.listdir(path)):
    if txt_file.endswith(".txt.txt"):
        aa = txt_file.split('-')
        if sub_nu in aa:
            txt_list.append(txt_file)

print (txt_list)

# extract the data from the Choice .txt.txt files and get the mean values for each categories
for t_file in txt_list:
    # unpack the scanlog txt file
    s_data = np.loadtxt(t_file, skiprows=7, usecols=(2, 4, 5, 6), dtype=dtype1)
    
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
     
    f.write(t_file + "\n")

    f.write("Category, RT_mean, Trail_mean, Response_mean \n")
     
    # Take out the tuple brackets
    f_mean =[', '.join(map(str, x)) for x in final_mean]

    # save the values to a file
    for i in f_mean:
        f.write( i + "\n")

    # f.write("++++++++++++++++++++++++++++++++++++++ \n")
    f.write("\n\n")
     
f.close()
     
     
    
