import csv
import pandas as pd
import numpy as np
import os
import sys

path = '/mnt/hcp01/scR21_asl/asl_results/ASL_CBF_values'

os.chdir(path)

files = sorted(os.listdir(path))

for fi in files:
    #df = pd.read_csv('CBF_values_50010_day_1.csv')
    df = pd.read_csv(fi)
    
    print (fi)
    print ("++++++++++++++++++++++++++++++++++")
    #for c in df:
    #	if str(c)=='1035' or str(c)=='2035':
    #		print (c, df[c][0], df[c][1])

    for c in df:
	if str(c)=="1035":# or str(c) == "2035":
        	print(c +"-ctx-lh-insula", df[c][0], df[c][1])
        if str(c)=="2035":
                print(c +"-ctx-rh-insula", df[c][0], df[c][1])
