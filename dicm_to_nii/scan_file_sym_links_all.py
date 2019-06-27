"""

     Developed by Sameera K Abeykoon
     To create symlinks - HCP unprocessed folders 
     fMRI, T1w and T2w folders to reference to fielmap files
     for FIELDMAP files in that FIELDMAP folder

"""

from __future__ import print_function
import numpy as np
import os, sys
import shutil
import pickle
import re

scan_file = sys.argv[1]
hcp_path = sys.argv[2]
#hcp_path = "/mnt/hcp01/pet_mri/vat_scz/50078"
#scan_file = "VAT_SCZ_10_31_scanlog.txt"

sub_num = os.path.basename(hcp_path)

# unpack the scanlog txt file
s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)

for i, j in enumerate(s_data[4]):
        
    # get the SpinEchoFieldMap files 
    if "fMRI" in j and "SBRef" not in j:

        field_num = s_data[5][i]
        #field_name = re.sub("fMRI_", "", j)
        #print (re.sub("fMRI_", "", j))
        field_name = j
        print (j)
        g_file = sub_num + "_3T_GradientEchoFieldMap.nii.gz"
        g_dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_GradientEchoFieldMap_" + str(field_num) + ".nii.gz"
        g_src = hcp_path + "/unprocessed/3T/" + field_name + "/" + g_file
        
        print (g_src)
        print (g_dst)
        if os.path.lexists(g_src):
            os.remove(g_src)
        os.symlink(g_dst, g_src)

        for i in range(2):
            if i == 0:
                spin_file = sub_num + "_3T_SpinEchoFieldMap_PA.nii.gz"
                ap_pa = "PA"
            else: 
                spin_file = sub_num + "_3T_SpinEchoFieldMap_AP.nii.gz"
                ap_pa = "AP"
        
            # This creates a symbolic link for FieldMap
            dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_SpinEchoFieldMap_" + ap_pa + "_" + str(field_num) + ".nii.gz"
            src = hcp_path + "/unprocessed/3T/" + field_name + "/" + spin_file
            #os.unlink(src)
            print (dst)
            print (src)
            if os.path.lexists(src):
                os.remove(src)
            os.symlink(dst, src)
            

    elif "T2w_SPC" in j or "T1w_MPR" in j:
        
        field_num = s_data[5][i]
        if "T2w_SPC" in j:
            field_name = re.sub("SPC_", "SPC", j)
        else:
            field_name = re.sub("MPR_", "MPR", j)
        
        g_file = sub_num + "_3T_GradientEchoFieldMap.nii.gz"
        g_dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_GradientEchoFieldMap_" + str(field_num) + ".nii.gz"
        g_src = hcp_path + "/unprocessed/3T/" + field_name + "/" + g_file

        print ("g_src",g_src)
        print ("g_dst",g_dst)

        if os.path.lexists(g_src):
            os.remove(g_src)
        if os.path.isdir(hcp_path + "/unprocessed/3T/" + field_name):
            os.symlink(g_dst, g_src)

        for i in range(2):
            if i == 0:
                spin_file = sub_num + "_3T_SpinEchoFieldMap_PA.nii.gz"
                ap_pa = "PA"
            else: 
                spin_file = sub_num + "_3T_SpinEchoFieldMap_AP.nii.gz"
                ap_pa = "AP"
        
            # This creates a symbolic link for FieldMap
            dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_SpinEchoFieldMap_" + ap_pa + "_" + str(field_num) + ".nii.gz"
            src = hcp_path + "/unprocessed/3T/" + field_name + "/" + spin_file
            #os.unlink(src)
            print (dst)
            print (src)
            if os.path.lexists(src):
                os.remove(src)
            if os.path.isdir(hcp_path + "/unprocessed/3T/" + field_name):
                os.symlink(dst, src)
