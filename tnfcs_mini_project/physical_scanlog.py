"""
    Developed by : Sameera Abeykoon (June 11 2018)
    This script will save the NYSPI incoming correct fMRI data, B0_fieldmaps
    T1w, T2w  into correct folders
    The correct data maybe in /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/"subject_number"/nii
    eg : /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/3045/nii
   
    This script needs PYTHON 3.5
    source activate py35_nib
"""

from __future__ import print_function
import numpy as np
import os, sys
import shutil
import re
import itertools as it
import dicom2nifti

# provide the Subject number
s_number = sys.argv[1]
#s_number =  input("Enter subject number ? ")
# s_number = "1491"

# copy use_scan.log file from the physical_disk to /mnt/jxvs01/pipelines/HCP/HCP_prep/XN_prep 
# scanlog.txt file
scan_file = "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" + s_number + "/use_scan.log"
scan_copy = "/mnt/jxvs01/pipelines/HCP/HCP_prep/XN_prep/" + s_number + "_scanlog.txt"
shutil.copyfile(scan_file, scan_copy)

with open(scan_copy) as f:
    arr = np.array(list(it.zip_longest(*[line.split() for line in f], fillvalue='0'))).T

# create HCP processed directory - tnfcs_PI
#hcp_dir = "/mnt/hcp01/tnfcs_PI/" + s_number
hcp_dir="/mnt/hcp01/tnfcs_mini/" + s_number
hcp_un_dir = hcp_dir + "/unprocessed"
hcp_un3T_dir = hcp_un_dir + "/3T"
hcp_field = hcp_un3T_dir + "/FieldMap"

if not os.path.exists(hcp_dir):
    os.mkdir(hcp_dir)
if not os.path.exists(hcp_un_dir):
    os.mkdir(hcp_un_dir)
if not os.path.exists(hcp_un3T_dir):
    os.mkdir(hcp_un3T_dir)
if not os.path.exists(hcp_field):
    os.mkdir(hcp_field)

# get the Nifti data folders
nii_path = "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" + s_number+ "/nii" # get the dicm2nii nii.gz files
fieldmap_path =  "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" + s_number + "/Fieldmap"
t1_path =  "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" +  s_number + "/T1"
t2_path =  "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/" +  s_number + "/T2"  

# Get a new filename to create AP and PA directions
volume_path = "/mnt/jxvs01/pipelines/HCP/projects/Pipelines/Examples/Scripts/templates/VolumeProcessingPipelineBatch_generator/"
filename =  volume_path + s_number + "_fMRI.txt"
ap_pa_file =  volume_path +  s_number + "_AP_PA.txt"

if os.path.exists(filename): os.remove(filename)
if os.path.exists(ap_pa_file): os.remove(ap_pa_file)      

# Write the AP or PA direction of the FMRI data
ap_file = open(ap_pa_file, "w")
ap_file.write("# " + scan_file)
ap_file.write('\n')

# Write the fMRI data
the_file = open(filename, "w")                              

j = 1
k = 1
l = 1

#  save the Nifti files into HCP folder in /mnt/hcp01/tnfcs_PI folder
for i in (arr):
    print ("protocol", i[4])
    # B0_fieldmap data 
    if "B0" in i[4]:
        b0_dir = fieldmap_path + "/" + i[1]
        field_file = hcp_field + "/" + s_number + "_3T_GradientEchoFieldMap_" + str(j) + ".nii.gz"
        dicom2nifti.dicom_series_to_nifti(b0_dir,field_file, reorient_nifti=True)
        j = j + 1

    # T1w data
    if "T1w" in i[4]:
        print ("T1w", k)
        t1w_dir = t1_path + "/" + i[1]
        t1mpr = hcp_un3T_dir + "/T1w_MPR" + str(k)
        if not os.path.exists(t1mpr):
            os.mkdir(t1mpr)
        t1_file = t1mpr + "/" + s_number + "_3T_T1w_MPR" + str(k) + ".nii.gz"
        dicom2nifti.dicom_series_to_nifti(t1w_dir,t1_file, reorient_nifti=True)
        k = k + 1
        # create symbolic link for GradientEchoFieldMap
        dst = hcp_field + "/" + s_number + "_3T_GradientEchoFieldMap_" + i[6] + ".nii.gz"
        src = t1mpr + "/" + s_number + "_3T_GradientEchoFieldMap.nii.gz"
        if os.path.lexists(src):
             os.remove(src)
        os.symlink(dst, src)

    # T2w data
    if "T2w" in i[4]:
        t2w_dir = t2_path + "/" + i[1]
        t2mpr = hcp_un3T_dir + "/T2w_SPC" + str(l)
        if not os.path.exists(t2mpr):
            os.mkdir(t2mpr)
        t2_file = t2mpr + "/" + s_number + "_3T_T2w_SPC" + str(l) + ".nii.gz"
        dicom2nifti.dicom_series_to_nifti(t2w_dir, t2_file, reorient_nifti=True)
        l = l + 1
        # create symbolic link for GradientEchoFieldMap
        dst = hcp_field + "/" + s_number + "_3T_GradientEchoFieldMap_" + i[6] + ".nii.gz"
        src = t2mpr + "/" + s_number + "_3T_GradientEchoFieldMap.nii.gz"
        if os.path.lexists(src):
             os.remove(src)
        os.symlink(dst, src)

    # fMRI data
    if "fMRI" in i[4]:
          fmri_dir = hcp_un3T_dir + "/" + i[4]
          if not os.path.exists(fmri_dir):
              os.mkdir(fmri_dir)
          niigz_file = nii_path + "/" + i[1] + ".nii.gz"
          # nii_file = nii_path + "/" + i[2] + ".nii"
          # copy the nii.gz file into the HCP fMRI folder
          if os.path.isfile(niigz_file):
              print ("Nifti file exits" , niigz_file)
              shutil.copyfile(niigz_file, fmri_dir + "/" + s_number + "_3T_" + i[4] + ".nii.gz")
          # create symbolic link for GradientEchoFieldMap
          dst = hcp_field + "/" + s_number + "_3T_GradientEchoFieldMap_" + i[6] + ".nii.gz"
          src = fmri_dir + "/" + s_number + "_3T_GradientEchoFieldMap.nii.gz"
          if os.path.lexists(src):
              os.remove(src)
          os.symlink(dst, src)
          # Write the fMRI data folder list
          the_file.write(i[4])
          the_file.write('\n')
          # Write the fMRI and AP and PA
          if int(i[7]) == 1:
              ap_file.write(i[4] + " " + "PA"+ '\n')
          else:
              ap_file.write(i[4] + " " + "AP" + '\n')

ap_file.close()
the_file.close()    
