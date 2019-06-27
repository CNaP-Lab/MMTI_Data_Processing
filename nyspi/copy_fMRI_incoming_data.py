"""
    Developed by : Sameera Abeykoon (June 11 2018)
    This script will save the NYSPI incoming correct fMRI data into correct folders
    The correct data maybe in /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/"subject_number"/nii
    eg : /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/3045/nii
    or MUX folder inside the subject number s ../XNAT_K01/horgconte/2264/12589/scans/10/MUX
"""

from __future__ import print_function
import numpy as np
import os, sys
import dicom
import shutil
import re

# provide the Subject numbers
s_number="3085"

# final Subject folder inside hcp01/tnfcs_PI
s_folder = s_number + "_B0EPI0"

# get the Nifti data folders
nii_path = "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" + s_number+ "/nii/" # get the dicm2nii nii.gz files

# scanlog file 
scan_file = s_number + "_scanlog_B0EPI0.txt"

# final data folder
fd_folder = "/mnt/hcp01/tnfcs_PI/" + s_folder

# final unprocessed data folder
dest_path="/mnt/hcp01/tnfcs_PI/" + s_folder + "/unprocessed/3T/"

# unpack the scanlog txt file
s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)

# get the scanlog file unpacked data
for i, j in enumerate(s_data[4]):
    if j.startswith('fMRI'):
        # get the folder path scanlog file (eg : 11119/scans/2/DICOM)
        path = s_data[1][i] 
        # get the folder number from the path (eg : 11119)
        param, value = path.split("/",1)
        # get the final folder number ( eg: 2)
        number = value.split("/")[1]
        
        # get the final data path inside the nii folder
        d_path = nii_path + "E" + param + "_S" + number + "_mux6_arc1.nii.gz"
        print (d_path)
        
        # if the nifiti file exists copy it to the final fMRI folder, 
        # if it is missing print that it is missing
        if os.path.exists(d_path):
            print (dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")
            shutil.copyfile(d_path , dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            print ("----------------------- Following data are missing ---------------------------")
            print ("data: ", s_folder + "_3T_"+ j + ".nii.gz")
            print ("fMRI folder: ",  dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")
            print ("-----------------------------------------------------------------------------") 


