from __future__ import print_function
import numpy as np
import os, sys
import glob

# provide the subject list
s_inputs = raw_input("Please enter the subjects list? eg [14701, 14702, ..] ")
s_inputs = eval(s_inputs)
log_folder = '/mnt/jxvs01/incoming/PET_MRI/VAT_SUD/logfiles'

os.chdir(log_folder)

for sb in s_inputs:
    file_list = glob.glob('Choice*' +  sb  +'*.txt.txt')
    for i in file_list:
    	cp = np.loadtxt(i, comments='#', delimiter=' ')
    

