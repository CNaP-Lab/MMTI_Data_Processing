"""
    Developed by : Sameera Abeykoon (May 30 2018)
    This script will save the NYSPI incoming correct fMRI data into correct folders
    The coorect data maybe in /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/"subject_number"/nii
    eg : /mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/3045/nii
    or MUX folder inside the subject number s ../XNAT_K01/horgconte/2264/12589/scans/10/MUX
"""


from __future__ import print_function
import os, sys
import shutil

# incoming data path "
data_path = "/mnt/jxvs01/incoming/NYSPI_data/physical_disk_K01/3056/nii"

#sub_no = raw_input("Enter subject number ? ")
# subject number "
sub_no = "3056"
in_data = raw_input("Enter incoming data .nii ? ")

# provide incoming data run number is it RS run 1, 2, 3 or 4 etc
in_no = raw_input("Enter the incoming data run number ? ")

# provide fMRI study name eg : SOT, TL, RS or CTA
fmri_name = raw_input("Enter fmri_name ? ")

f_names = ("_Spin0EPI0", "_Spin5EPI0", "_Spin0EPI5", "_Spin5EPI5", "_B0EPI5", "_B0EPI0")

for i in range(6):
    # get the fMRI folder name
    folder = sub_no + f_names[i]
    # get the final data destination path
    dest_path = "/mnt/hcp01/tnfcs_PI/"+ folder+"/unprocessed/3T/fMRI_" + fmri_name + "_" + str(in_no)

    print (data_path + "/" + in_data)
    print (dest_path + "/" + folder + "_3T_fMRI_" + fmri_name + "_" + str(in_no) + ".nii.gz")
    # copy the data into correct fMRI folders
    shutil.copyfile(data_path + "/" + in_data, dest_path + "/" + folder + "_3T_fMRI_" + fmri_name + "_" + str(in_no) + ".nii.gz")
