"""
    Developed by : Sameera Abeykoon (March 2019)
    Create symlink for tnfcs_mini data after copying data from
    tnfcs or tnfcs_PI subject folders

    python tnfcs_mini_symlink.py "50006"  
    python tnfcs_mini_symlink.py
"""

from __future__ import print_function
import numpy as np
import os, sys

if len(sys.argv) > 1:
    s_number = sys.argv[1]
else:
    # provide the Subject numbers
    s_number = raw_input("Enter subject number example 50006? ")

print ("Subject number is ", s_number)

# final Subject folder inside mnt/hcp01/tnfcs_mini/
s_folder = "/mnt/hcp01/tnfcs_mini/" + s_number + "/unprocessed/3T/"

# Finelmap folder
f_folder = "/mnt/hcp01/tnfcs_mini/" + s_number + "/unprocessed/3T/FieldMap/"

os.chdir(s_folder)

list_dir = next(os.walk('.'))[1]
sb_ap_file = s_number + "_3T_SpinEchoFieldMap_AP.nii.gz"
sb_pa_file = s_number + "_3T_SpinEchoFieldMap_PA.nii.gz"
print (sb_ap_file, sb_pa_file)
# get the scanlog file unpacked data
for x in list_dir:
    if 'fMRI' in x:
        print ("fMRI", x)
        # change into fMRI or T1w or T2w folders
        os.chdir(x)
        
        # get the AP and PA file paths
        ap_path = s_folder + x + "/" + sb_ap_file
        pa_path = s_folder + x + "/" + sb_pa_file

        # get the symlink of AP file and PA file
        ap_link = os.readlink(ap_path)
        pa_link = os.readlink(pa_path)
        
        # basename of the symlink
        ap_base = os.path.basename(ap_link)
        pa_base = os.path.basename(pa_link)
        
        # extract number from String in symlink
        ap_int = (filter(str.isdigit, ap_base))[-1]
        pa_int = (filter(str.isdigit, ap_base))[-1]
        print (ap_int, pa_int)
        
        src_ap = s_folder + "FieldMap/" + s_number + "_3T_SpinEchoFieldMap_AP_" + ap_int + ".nii.gz"
        src_pa = s_folder + "FieldMap/" + s_number + "_3T_SpinEchoFieldMap_PA_" + pa_int + ".nii.gz"
        
        if os.path.islink(ap_path):
            os.unlink(ap_path)

        if os.path.islink(pa_path):
            os.unlink(pa_path)

        os.symlink(src_ap, ap_path)
        os.symlink(src_pa, pa_path)

        # change into unprocessed 3T folder
        os.chdir(s_folder)
    elif "T1w" in x or "T2w" in x:
        print ("T1w or T2w", x)
        # change into fMRI or T1w or T2w folders
        os.chdir(x)
        
        # get the AP and PA file paths
        ap_path = s_folder + x + "/" + sb_ap_file
        pa_path = s_folder + x + "/" + sb_pa_file

        # get the symlink of AP file and PA file
        ap_link = os.readlink(ap_path)
        pa_link = os.readlink(pa_path)
        
        # basename of the symlink
        ap_base = os.path.basename(ap_link)
        pa_base = os.path.basename(pa_link)
        
        # extract number from String in symlink
        ap_int = (filter(str.isdigit, ap_base))[-1]
        pa_int = (filter(str.isdigit, ap_base))[-1]
        print (ap_int, pa_int)

        src_ap = s_folder + "FieldMap/" + s_number + "_3T_SpinEchoFieldMap_AP_" + ap_int + ".nii.gz"
        src_pa = s_folder + "FieldMap/" + s_number + "_3T_SpinEchoFieldMap_PA_" + pa_int + ".nii.gz"
        
        if os.path.islink(ap_path):
            os.unlink(ap_path)

        if os.path.islink(pa_path):
            os.unlink(pa_path)

        os.symlink(src_ap, ap_path)
        os.symlink(src_pa, pa_path)
        
        # change into unprocessed 3T folder
        os.chdir(s_folder)
    elif "FieldMap" in x:
        print ("FieldMap")
       # os.chdir(x)
   
