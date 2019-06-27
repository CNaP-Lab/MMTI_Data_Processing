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

#scan_file = sys.argv[1]
#hcp_path = sys.argv[2]
hcp_path = "/mnt/hcp01/pet_mri/vat_scz/50036"
scan_file = "VAT_SCZ_10_24_scanlog.txt"

sub_num = os.path.basename(hcp_path)
# sub_num="50036"
# unpack the scanlog txt file
s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)

for i, j in enumerate(s_data[4]):
        
    # get the SpinEchoFieldMap files 
    """if "fMRI" in j and "SBRef" in j:
        if s_data[4][i+1] in j:
             print (s_data[4][i+1], j)
             if s_data[7][i+1] == 1:
                spin_file = sub_num + "_3T_SpinEchoFieldMap_PA.nii.gz"
                ap_pa = "PA"
             else:
                spin_file = sub_num + "_3T_SpinEchoFieldMap_AP.nii.gz"
                ap_pa = "AP"
             field_num = s_data[5][i+1]
   
             # This creates a symbolic link for FieldMap
             dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_SpinEchoFieldMap_" + ap_pa + "_" +  str(field_num) + ".nii.gz"
             src = hcp_path + "/unprocessed/3T/" + s_data[4][i+1] + "/" + spin_file
             print (dst)
             print (src)
             if os.path.lexists(src):
                 os.remove(src)
             os.symlink(dst, src)"""
      
    if "fMRI" in j and "SBRef" not in j:
       
        spin_file = sub_num + "_3T_SpinEchoFieldMap_PA.nii.gz"
        ap_pa = "PA"
        spin_file = sub_num + "_3T_SpinEchoFieldMap_AP.nii.gz"
        ap_pa = "AP"
        field_num = s_data[5][i]
        field_name = re.sub("fMRI_", "", j)
        print (re.sub("fMRI_", "", j))
   
        # This creates a symbolic link for FieldMap
        dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_SpinEchoFieldMap_" + ap_pa + "_" + str(field_num) + ".nii.gz"
        src = hcp_path + "/unprocessed/3T/" + field_name + "/" + spin_file
        #os.unlink(src)
        print (dst)
        print (src)
        if os.path.lexists(src):
            os.remove(src)
        os.symlink(dst, src)
        #os.symlink(dst, src)

    elif "T2w_SPC" in j or "MPRAGE_CUBIT_p87m" in j:
        
        field_num = s_data[5][i]
        if "T2w_SPC" in j:
            field_name = re.sub("SPC_", "SPC", j)
        else:
            field_name = re.sub("MPR_", "MPR", j)
   
        # This creates a symbolic link for FieldMap
        dst = hcp_path + "/unprocessed/3T/FieldMap/" + sub_num + "_3T_SpinEchoFieldMap_" + ap_pa + "_" +  str(field_num) + ".nii.gz"
        src = hcp_path + "/unprocessed/3T/" + field_name + "/" + spin_file
        print (dst)#os.unlink(src)
        print (src)
        if os.path.lexists(src):
            os.remove(src)
        os.symlink(dst, src)
      
        


