from __future__ import print_function
import os, time, string
import dicom
import sys

#  Please provide the path to the data directory
# example: ipython create_scanlog_SB.py /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3046_V26_JV

# topdir=/mnt/jxvs01/incoming/JVS_K01_VanSnellenberg
# tobedone=S3046_V26_JV

path = sys.argv[1]

topdir,tobedone = os.path.split(path)
print ("Incoming data directory path", topdir)   
print ("Subject data directory ", tobedone)

current_dir = topdir
past_dir = topdir
alldir = []

allstudy = []
allstring = []

mapoutlist = []
mapoutcont = []
mapouttype = []
mapoutlabel = []
mapoutsnum = []
mapoutextra = []

allfunc = []
allb0 = []
allap = []
allpa = []
allt1 = []
allt2 = []

# Files can come with different file extension
# DICOM has .dcm or .IMA
f_ext = (".dcm", "IMA")

fmri=('FMRI', 'fMRI', 'fmri')
print(os.listdir(path))
print ("++++++++++++++++++++++++++++")

while os.path.isdir(current_dir):
    breakout = 0
    
    for i in os.listdir(current_dir):
        
        #if current_dir == topdir and i not in tobedone:
        #    continue
        next_level = current_dir + '/' + i
        if os.path.isdir(next_level):
            if next_level in alldir:
                continue
            else:
                past_dir = current_dir
                current_dir = next_level
                breakout = 1
                break
       
        elif next_level.endswith(tuple(f_ext)):

            splitup = next_level.split('/')

            dcmhdr = dicom.read_file(next_level)
            filenum = int(dcmhdr['0020','0011'].value)
            filename = dcmhdr['0008','103e'].value
            
            # filename given example: fMRI_Resting_1_AP, T1W_MPR
            print (filename)
            # print (dcmhdr['0020','0011'].value
