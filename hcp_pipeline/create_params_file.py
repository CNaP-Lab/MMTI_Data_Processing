"""
Created By: Sameera Abeykoon
This will create the HCP params(example:
S3071_V15_AAD_HCP_prep_script.params)
input file for follwoing 3 c-shell scripts
HCP_anatomy_prep.csh
HCP_fielMap_prep.csh  
HCP_fMRI_prep.csh
""" 
import io
import sys
import os

# subject number example : 50022
# subject directory full path /mnt/hcp01/tnfcs/50022

# Enter the full path to the final data analysed folder"
subjdir=raw_input("Enter the subject directory full path ? ")

subjid=os.path.basename(subjdir)

# Enter the full path to the DICOM files, which copied from the
# SCAN_center 
# example /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3060_JV
dcm_dir=raw_input("Enter the incoming data directory full path ? ")

# get the data id given from the SCAN_center
data_id=os.path.basename(dcm_dir)

# get the current directory path
cwd = os.getcwd()

# save these details to the HCP_prep.params file
f=open(data_id+"_HCP_prep_script.params", "w")

f.write("set subjid = "+subjid+"\n")
f.write("set subjdir = "+subjdir+"\n")
f.write("set xnat_dir = "+dcm_dir+"\n")
f.write("set dcm_dir = "+dcm_dir+"\n")
f.write("set nii_dir = "+dcm_dir+"\n")
f.write("set scanlog = "+cwd+"/"+data_id+"_scanlog.txt\n")
f.write("set xnatmode = 0\n")
f.write("set slicetime = 0\n")

f.close()
