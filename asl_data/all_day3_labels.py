"""
Developed by Sameera K. Abeykoon (January 2019)
To extarct all 3 days CBF values files and put 
togather all the data into one file with
label numbers and lable names.


"""

import csv
import io
import sys
import os
import numpy as np

sub_no=input("Enter the subject number ? ")
#day1_f=input("Enter the day1 CBF values .csv file ? ")
#day2_f=input("Enter the day2 CBF values .csv  file ? ")
#day3_f=input("Enter the day3 CBF values .csv file ? ")

day1_f = "CBF_values_"+ str(sub_no) + "_day_1.csv"
day2_f = "CBF_values_"+ str(sub_no) + "_day_2.csv"
day3_f = "CBF_values_"+ str(sub_no) + "_day_3.csv"

# extract CBF csv files
if os.path.isfile(day1_f):
    with open(day1_f, newline='') as csvfile:
        data1 = list(csv.reader(csvfile))
else:
    data1 = np.zeros((3, 3))
if os.path.isfile(day2_f):
    with open(day2_f, newline='') as csvfile:
        data2 = list(csv.reader(csvfile))
else:
    data2 = np.zeros((3, 3))
if os.path.isfile(day3_f):
    with open(day3_f, newline='') as csvfile:
        data3 = list(csv.reader(csvfile))
else:
    data3 = np.zeros((3, 3))

with open('label_numbers.csv') as f:
    lis_lab = [x.split() for x in f]
      
labels = list(zip(*lis_lab))

# create a new file to extract data
new_csv = sub_no + "_labels_all3Days_CBF.csv"

with open(new_csv, mode='w') as csv_file:
    fieldnames = ['label_num', 'label_name', 'day-1_CBF-mean', 'day-1_CBF-std', 'day-2_CBF-mean', 'day-2_CBF-std', 'day-3_CBF-mean', 'day-3_CBF-std']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for k, name in enumerate(labels[0]):
        if name in data1[0]:
            index = data1[0].index(name)
            d1_mean = data1[1][index]
            d1_std = data1[2][index]
        else:
            d1_mean = 0
            d1_std = 0
        if name in data2[0]:
            index = data2[0].index(name)
            d2_mean = data2[1][index]
            d2_std = data2[2][index]
        else:
            d2_mean = 0
            d2_std = 0
        if name in data3[0]:
            index = data3[0].index(name)
            d3_mean = data3[1][index]
            d3_std = data3[2][index]
        else:
            d3_mean = 0
            d3_std = 0
            
        print (name,labels[2][k], d1_mean, d1_std, d2_mean, d2_std, d3_mean, d3_std)
        writer.writerow({'label_num':name, 'label_name': labels[2][k], 'day-1_CBF-mean': d1_mean, 'day-1_CBF-std':d1_std, 'day-2_CBF-mean':d2_mean, 'day-2_CBF-std':d2_std, 'day-3_CBF-mean':d3_mean, 'day-3_CBF-std':d3_std})
