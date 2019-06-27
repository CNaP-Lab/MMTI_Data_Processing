from __future__ import print_function
import numpy as np
import os, sys
import dicom
import shutil

path = sys.argv[2]
scan_file = sys.argv[1]

topdir,tobedone = os.path.split(path)
print ("Incoming data directory path", topdir)
print ("Subject data directory ", tobedone)

# create a directory to save SBRef files
Sb_path="/mnt/jxvs01/incoming/NYSPI_SBref/XNAT_K01/horgconte/"+tobedone
if not os.path.exists(Sb_path):
	os.makedirs(Sb_path)

# Files can come with different file extension
# DICOM has .dcm or .IMA
f_ext = (".dcm", "IMA")

# unpack the scanlog txt file
s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)
#print (s_data[4])

# Get a new filename to create AP and PA directions
filename = os.path.splitext(os.path.basename(scan_file))[0] + "_AP_PA.txt"
file_scanlog = os.path.splitext(os.path.basename(scan_file))[0] + "_SBRef.txt"

# If exist remove the AP_PA.txt file
try:
    os.remove(filename)
    print ("removed filename")
except OSError:
    pass

# If exist remove scanlog_SBRef.txt file
try:
    os.remove(file_scanlog)
    print ("removed file_scanlog")
except OSError:
    pass

# Find the PA and AP orientation for Volume processing
with open(filename, 'a') as the_file:
	the_file.write(scan_file)
        the_file.write('\n')
        for i, j in enumerate(s_data[4]):
		if j.startswith("fMRI"):
                        if s_data[7][i] == str(2):
                          the_file.write(j + ' '+ "AP")
                          the_file.write('\n')
                        else:
                          the_file.write(j + ' '+ "PA")
                          the_file.write('\n')

# This will create SBRef files using Topup folder 1st file in NYSPI_SbRef folder
#with open(file_scanlog, 'a') as s_file:
#    count = 1
for i, j in enumerate(s_data[4]):
	if j == "Topup_PA":
           #print ("Topup_PA")
           dicm_path = path + '/' + s_data[1][i]
           Sb_path_no = Sb_path + "/" +  s_data[5][i] + "/Topup_PA"
           if not os.path.exists(Sb_path_no):
           	os.makedirs(Sb_path_no)
           # copy the first .dcm file from Topup_PA for SBRef file
	   for fname in os.listdir(dicm_path):
                    if fname.endswith(tuple(f_ext)):
                         file_path = dicm_path + "/" + fname
                         #print ("file_path", file_path)
                         shutil.copyfile(file_path, Sb_path_no + "/" + fname)
                         break
	   # s_file(count + ' ' +  + "12:00" + ' ' +
        elif j == "Topup_AP":
           #print ("Topup_AP")
           #print (path + '/' + s_data[1][i])
           dicm_path = path + '/' + s_data[1][i]
           Sb_path_no = Sb_path + "/" +  s_data[5][i] + "/Topup_AP"
           if not os.path.exists(Sb_path_no):
                os.makedirs(Sb_path_no)
           # copy the first .dcm file from Topup_PA for SBRef file
           for fname in os.listdir(dicm_path):
                    if fname.endswith(tuple(f_ext)):
                         file_path = dicm_path + "/" + fname
                         #print ("file_path", file_path)
                         shutil.copyfile(file_path, Sb_path_no + "/" + fname)
                         break

save_path = "/mnt/jxvs01/incoming/NYSPI_SBref/XNAT_K01/horgconte/"
with open(file_scanlog, 'a') as s_file:
    count = 0
    # get SBRef file for each fMRI run
    for i, j in enumerate(s_data[4]):
        print (j)
        if j.startswith("fMRI"):
            count += 1
            # check whether PA or AP
            if s_data[7][i] == str(2):
              T_dir = "Topup_AP"
              print ("T_dir", T_dir)
              s_file.write(str(count) + ' ' + s_data[5][i]+"/"+T_dir + " " + "12:00" + ' ' + j+"_SBRef" + ' ' + j+"_SBRef" + ' ' + s_data[5][i] + ' ' + s_data[6][i] + ' ' + s_data[7][i])
              s_file.write("\n")
            else:
              T_dir = "Topup_PA"
              print ("T_dir", T_dir)
              s_file.write(str(count) + ' ' + s_data[5][i]+"/"+T_dir + " " + "12:00" + ' ' + j+"_SBRef" + ' ' + j+"_SBRef" + ' ' + s_data[5][i] + ' ' + s_data[6][i] + ' ' + s_data[7][i])
              s_file.write("\n")
        #count += 1
