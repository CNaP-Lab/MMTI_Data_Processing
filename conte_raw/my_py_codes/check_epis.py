from __future__ import print_function
import os, io
import numpy as np

path = "/mnt/jxvs02/conte_processed_data/preprocessing_data_02222012"
#os.chdir(path)

number = 1020
file4 = open("SO_study4.txt","w") 
file5 = open("SO_study5.txt","w") 

for dir_n in sorted(os.listdir(path)):
    dir_path = path + "/" + dir_n + "/EPIs"
    splitup = dir_n.split("_")
    if splitup[0][1] == str(3):
       if splitup[2] == str(1):
          day = "day_1"
       elif splitup[2] == str(2):
          day = "day_2"
       else:
          print ("wrong Day  +++++++++++++++++++++++++")
       study = "SO_study3_rawdata/" + splitup[1] + "_DAR" + str(number) + "/" + day
       number = number + 1
    elif splitup[0][1] == str(4):
       study = "SO_study4_rawdata/" + splitup[1]
    elif splitup[0][1] == str(5):
       study = "SO_study5_rawdata/" + splitup[1]
    else:
       print ("Wrong STUDY ****************************")
 
    print (dir_path)
    for fname in sorted(os.listdir(dir_path)):
        con_data_path = "/mnt/hcp01/conte_raw_data/" + study + "/scan_data/" + fname
        f_path = dir_path + "/" + fname
       
        if splitup[0][1]  == str(4):
            file4.write(fname)
            file4.write("\n")
            file4.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            file4.write("\n")
            if os.path.isfile(con_data_path):
        	con_data_path = "/mnt/hcp01/conte_raw_data/" + study + "/scan_data/" + fname
                file4.write("file exits \n ")
            else:
    		file4.write("file missing \n")


        if splitup[0][1]  == str(5):
            file5.write(fname)
            file5.write("\n")
            file5.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            file5.write("\n")
            if os.path.isfile(con_data_path):
        	con_data_path = "/mnt/hcp01/conte_raw_data/" + study + "/scan_data/" + fname
                file5.write("file exits \n ")
            else:
    		file5.write("file missing \n")
    		


file4.close() 
file5.close() 
