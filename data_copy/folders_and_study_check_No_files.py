from __future__ import print_function
import os, time, string
import dicom
import sys
import numpy as np
import shutil

"""
   Developed By Sameera K. Abeykoon (March , 2018)
   This will provide the filename(protocal name) and the
   folder name and if it's T1w or T2w it will provide the 
   more detils to use in scanlog text

Please provide the path to the data directory
example: ipython create_scanlog_SB.py /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3046_V26_JV

    topdir=/mnt/jxvs01/incoming/JVS_K01_VanSnellenberg
    tobedone=S3046_V26_JV                                                                   
"""

path = sys.argv[1]

topdir,tobedone = os.path.split(path)
print ("Incoming data directory path", topdir)   
print ("Subject data directory ", tobedone)

study = os.path.split(topdir)[1]

# Files can come with different file extension
# DICOM has .dcm or .IMA
f_ext = (".dcm", ".IMA", ".ima")

c_folder = [ ]
dir_folder = [ ]


# Get the study name
scan_data = study + "_" + tobedone + "_folder_names.csv"
f = open(scan_data ,"w+")
f.write(("filename" +"\tNumber of files" + "\tfolder name \n"))
missing_files = [ ]
missing_no = [ ]

for i in np.sort(os.listdir(path)):
        
        if os.path.isdir(path + "/" + i):
            print ("Current folder ", (path+"/"+i))

            for fname in os.listdir(path+"/"+i):
                    if fname.endswith(tuple(f_ext)):
                        next_level = path + "/" + i + "/" + fname 
                        break
             
            #for fname in os.listdir(path + "/" + i):
            #    if fname.endswith(tuple(f_ext)):
            #        next_level = path + "/" + i + "/" + fname
            #            break
       
            splitup = next_level.split('/')
            
            list_no = len(os.listdir(path + "/" + i))
            print ("Number of files", list_no)

            dcmhdr = dicom.read_file(next_level)
            filenum = int(dcmhdr['0020','0011'].value)
            filename = dcmhdr['0008','103e'].value
            #TR = dcmhdr['0018', '0080'].value # Repetition Time
            #TE = dcmhdr['0018', '0081'].value # Echo Time
            
            # filename given example: fMRI_Resting_1_AP, T1W_MPR
            print ("filename", filename)
            c_folder.append(filename)
            dir_folder.append(i)
            
            # DICOM directory name (long number)
            mapoutname = str(splitup[6])
            print ("folder number", mapoutname)
           
            print ("+++++++++++++++++++++++++++++++++++++++")

            if "physio" in i:
                print ("Exclude physio directory")
            elif "CTA_PSD" in filename:
                if "SBRef" in filename:
                    if int(list_no) == 2:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 3:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
                else:
                    if int(list_no) == 432:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 433:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
            elif "CTA_thalloc" in filename:
                if "SBRef" in filename:
                    if int(list_no) == 2:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 3:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
                else:
                    if int(list_no) == 114:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 115:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
            elif "Resting" in filename:
                if "SBRef" in filename:
                    if int(list_no) == 2:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 3:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
                else:
                    if int(list_no) == 1126:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 1127:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
            elif "SOT" in filename:
                if "SBRef" in filename:
                    if int(list_no) == 2:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 3:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
                else:
                    if int(list_no) == 1152:
                        print ("Number of files are there :", list_no)
                    elif int(list_no) == 1153:
                        print ("Number of files are there :", list_no)
                    else:
                        missing_no.append(filename)
                        missing_no.append(list_no)
            elif "T1w_MPR" in filename:
                if int(list_no) == 416:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 417:
                    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no)
            elif "T2w_SPC" in filename:
                if int(list_no) == 416:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 417:
                    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no)
            elif "SpinEchoFieldMap_AP" in filename:
                if int(list_no) == 6:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 7:
                    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no)
            elif "SpinEchoFieldMap_PA" in filename:
                if int(list_no) == 6:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 7:
                    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no)
            elif "field_map_EPI" in filename:
                if int(list_no) == 264:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 132:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 265:
                    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no) 
            elif "hx_gre_MT_PKC3_10MEAS" in filename:
                if int(list_no) == 200:
                    print ("Number of files are there :", list_no)
                #elif int(list_no) == 132:
                #    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no) 
            elif "AdjGre" in filename:
                if int(list_no) == 258:
                    print ("Number of files are there :", list_no)
                #elif int(list_no) == 132:
                #    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no) 
            elif "Localizer" in filename:
                if int(list_no) == 6:
                    print ("Number of files are there :", list_no)
                elif int(list_no) == 7:
                    print ("Number of files are there :", list_no)
                else:
                    missing_no.append(filename)
                    missing_no.append(list_no) 
            
            f.write("%s\t%s\t%s\n" % (filename, int(list_no), i))

f.write("\n\n\n")
f.write("------------Informtaion about Missing Files-----------\n")
f.write("------------------------------------------------------\n\n")
print (c_folder)

for k in missing_no:
    f.write("%s\n" % (k))

#  Check the CTA_PSD, THL, SOT and REST file numbers in the scan
psd = 0
thl = 0
rest = 0
sot = 0
psd_sb = 0
thl_sb = 0
rest_sb = 0
sot_sb = 0

for k, j in enumerate(c_folder):
    if "CTA_PSD" in j and "SBRef" not in j:
        if dir_folder[k] != "physio":
            psd += 1
    elif "CTA_PSD" in j and "SBRef" in j:
        psd_sb += 1
    elif "CTA_thalloc" in j and "SBRef" not in j:
        if dir_folder[k] != "physio":
            thl += 1
    elif "CTA_thalloc" in j and "SBRef" in j:
        thl_sb += 1
    elif "Resting" in j and "SBRef" not in j:
        if dir_folder[k] != "physio":
            rest += 1
    elif "Resting" in j and "SBRef" in j:
        rest_sb += 1
    elif "SOT" in j and "SBRef" not in j:
        if dir_folder[k] != "physio":
            sot += 1
    elif "SOT" in j and "SBRef" in j:
        sot_sb += 1
       
try:
   print ("PSD ", psd)
   if int(psd) != 6:
        f.write("CTA PSD files are missing %s\n" % (int(psd)))
   elif int(psd_sb) != 6:
        f.write("CTA PSD SBRef files are missing %s\n" % (int(psd_sb)))
except:
   print ("NO PSD files")

try:
   print ("THL ", thl)
   if int(thl) != 4:
        f.write("CTA THL files are missing %s\n" % (int(thl)))
   elif int(thl_sb) != 4:
        f.write("CTA THL SBRef files are missing %s\n" % (int(thl_sb)))
except:
   print ("NO THL files")

try:
   print ("Resting  ", rest)
   if int(rest) != 4:
        f.write("Resting files are missing %s\n" % (int(rest)))
   elif int(rest_sb) != 4:
        f.write("Resting SBRef files are missing %s\n" % (int(rest_sb)))
except:
   print ("NO REST files")

try:
   print ("SOT  ", rest)
   if int(sot) != 4:
        f.write("SOT files are missing %s\n" % (int(sot)))
   elif int(sot) != 4:
        f.write("SOT SBRef files are missing %s\n" % (int(sot_sb)))
except:
   print ("NO SOT files")

f.close()

# Move .csv files into SB_prep/scan_details folder
src_file = "/mnt/jxvs01/pipelines/HCP/HCP_prep/SB_prep/" + scan_data
dest_file = "/mnt/jxvs01/pipelines/HCP/HCP_prep/SB_prep/scan_details/" + scan_data

shutil.move(src_file, dest_file)
