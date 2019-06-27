from __future__ import print_function
import numpy as np
import os
import sys
import dicom
import shutil
import re
import nibabel as nib

# provide the Subject numbers
s_number = input("Enter subject number ? ")
#s_number="3057"

# final Subject folder inside hcp01/tnfcs_PI
s_folder = s_number # + "_B0EPI0"

# final data folder
fd_folder = "/mnt/hcp01/tnfcs_PI/" + s_folder + "/unprocessed/3T"

# change the fMRI data folders
# os.chdir(fd_folder)

for l_dir in os.listdir(fd_folder):
    if 'fMRI' in l_dir:
        l_path = fd_folder + "/" + l_dir
        os.chdir(l_path)
        for f in os.listdir('.'):
              if 'fMRI' in f:
                   f_path = fd_folder + "/" + l_dir
                   f_nim = nib.load(f)
                   print (f)
                   print ("Old file dim", f_nim.header['dim'])
                   print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                   
                   f_nim2 = nib.Nifti1Image(f_nim.get_fdata()[..., 2:], f_nim.get_affine(), f_nim.header)
                   #shutil.move(os.path.join(f_path, f), os.path.join(f_path, f_nim2))
                   #os.remove(f)
                   fname = os.path.join(f_path, f)
                   nib.save(f_nim2, fname)

                   #shutil.copyfile(f_nim2, f_path)
                   f_nim3 = nib.load(f)
                   print ("New file dim", f_nim3.header['dim'])
                   print ("----------------------------------------------------------------")
                   print ("                                                                ")
                   os.chdir('../')
