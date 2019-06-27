"""
	Developed by Sameera K. Abeykoon ( July 10th 2018)
        This script will skip the volumes from the .nii.gz file
"""

from __future__ import print_function
import numpy as np
import os
import sys
#import dicom
import shutil
import re
import nibabel as nib


def skip_first_volumes(s_folder, fd_folder, no_skip=2):
    """
    Parameters
    ----------
    s_folder : str
               the Subject numbers
    fd_folder : str 
               final data folder
    no_skip : int, optional
              number of volumes to skip
    """
    
    for l_dir in os.listdir(fd_folder):
    	if 'fMRI' in l_dir:
            l_path = fd_folder + "/" + l_dir
            os.chdir(l_path)
            for f in os.listdir('.'):
                if 'fMRI' in f:# and 'SOT_fMRI_3' in f and 'SOT_fMRI_2' in f:
                    f_path = fd_folder + "/" + l_dir
                    f_nim = nib.load(f)
                    print (f)
                    print ("Old file dim", f_nim.header['dim'])
                    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                   
                    f_nim2 = nib.Nifti1Image(f_nim.get_fdata()[..., no_skip:], f_nim.get_affine(), f_nim.header)
                    fname = os.path.join(f_path, f)
                    nib.save(f_nim2, fname)

                    #shutil.copyfile(f_nim2, f_path)
                    f_nim3 = nib.load(f)
                    print ("New file dim", f_nim3.header['dim'])
                    print ("----------------------------------------------------------------")
                    print ("                                                                ")
                    os.chdir('../')

    

if __name__ == "__main__":

    # provide the Subject numbers
    s_folder = input("Enter subject number ? ")
    #s_number="3057"

    # final Subject folder inside hcp01/tnfcs_PI
    # s_folder = s_number # + "_B0EPI0"
    
    # final data folder
    fd_folder = "/mnt/hcp01/tnfcs_PI/" + str(s_folder) + "/unprocessed/3T"

    # provide number of volumes to skip
    # no_skip = input("Enter number of volumes to skip ? ")
    #s_number="2"
    
    no_skip = 2
    skip_first_volumes(str(s_folder), fd_folder, no_skip)
