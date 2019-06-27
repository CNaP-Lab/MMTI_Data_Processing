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
import gzip

# provide the Subject numbers
s_number = raw_input("Enter subject number ? ")
#s_number="3057"

# final Subject folder inside hcp01/tnfcs_PI
s_folder = s_number #+ "_B0EPI0"

# get the NYSPI data folder
nys_path = "/mnt/jxvs01/incoming/NYSPI_data/XNAT_K01/horgconte/" + s_number # get the dicm2nii nii.gz files

# scanlog file 
scan_file = s_number + "_scanlog.txt"

# final data folder
fd_folder = "/mnt/hcp01/tnfcs_PI/" + s_folder

# final unprocessed data folder
dest_path="/mnt/hcp01/tnfcs_PI/" + s_folder + "/unprocessed/3T/"

# unpack the scanlog txt file
s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)

print (s_data[4])

# get the scanlog file unpacked data
for i, j in enumerate(s_data[4]):
    if 'fMRI' in j:
        # get the folder path scanlog file (eg : 11119/scans/2/DICOM)
        s_path = s_data[1][i] 
        # get the folder number from the path (eg : 11119)
        param, value = s_path.split("/",1)
        # get the final folder number ( eg: 2)
        number = value.split("/")[1]
        
        # get the folder path scanlog file (eg : 11119/scans/2/DICOM)
        # take out the "DICOM"
        path_v = s_data[1][i].split("/")
        dicom = path_v.pop()

        # folder path
        path = '/'.join([str(x) for x in path_v]) 

        mux_path = nys_path + "/" + path + "/MUX/" 
        
        # get the final data path inside the nii folder
        try:
            mux_path + "E" + param + "_S" + number + "_mux6_arc1.nii.gz"
        except:
            print ("nii.gz is not here")
        else:
            mux_path + "E" + param + "_S" + number + "_mux6_arc1.nii"

        m_path = mux_path + "E" + param + "_S" + number + "_mux6_arc1.nii.gz"
        mn_path = mux_path + "E" + param + "_S" + number + "_mux6_arc1.nii"
        print (m_path)
        
        if os.path.exists(dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz"):
            os.remove(dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")

        # if the nifiti file exists copy it to the final fMRI folder, 
        # if it is missing print that it is missing
        if os.path.exists(m_path):
            print (" NII.gz file exists ")
            print (" ===================")
            
            shutil.copyfile(m_path , dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")
            
            print (dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")

            print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif os.path.exists(mn_path):
            print (" NII file exists   ")
            print (" =================")

            shutil.copyfile(mn_path , dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii")
            gzip.compress(dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii")
            
            if os.path.exists(dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz"):
            	print (dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz      EXISTS")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        else:
            print ("----------------------- Following data are missing ---------------------------")
            print ("data: ", s_folder + "_3T_"+ j + ".nii.gz")
            print ("fMRI folder: ",  dest_path +  j+"/" + s_folder + "_3T_"+ j + ".nii.gz")
            print ("-----------------------------------------------------------------------------") 


