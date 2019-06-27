from __future__ import print_function
import numpy as np
import os, sys

path = sys.argv[2]
scan_file = sys.argv[1]

# unpack the scanlog txt file
s_data = np.genfromtxt(scan_file, delimiter=" ", dtype=str, unpack=True)

# Get a new filename to create AP and PA directions
filename = os.path.splitext(os.path.basename("S3162_V30_ADD_scanlog.txt"))[0] + "_AP_PA.txt"

with open(filename, 'a') as the_file:
	the_file.write(scan_file)
        the_file.write('\n')
        for i, j in enumerate(s_data[3]):
		if j.startswith("fMRI") and not j.endswith("SBRef"):
        	      the_file.write('\n')
                      if s_data[7][i] == str(1):
                          the_file.write(j + " " + "AP")
                      else:
                          the_file.write(j + " " + "PA")
