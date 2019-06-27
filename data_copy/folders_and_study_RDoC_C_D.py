from __future__ import print_function
import os, time, string
import dicom
import sys
import numpy as np
import glob
import fnmatch

# Developed By Sameera K. Abeykoon (March , 2018)
# 

def income_data_extract_D(path):
    topdir,tobedone = os.path.split(path)
    print ("Incoming data directory path", topdir)   
    print ("Subject data directory ", tobedone)

    # Files can come with different file extension
    # DICOM has .dcm or .IMA
    f_ext = (".dcm", ".IMA", ".ima")

    c_folder = [ ]
    f = open(tobedone + "_folder_names.csv","w+")
    f.write(("filename" +"\tNumber of files" + "\tfolder name \n"))
    mrs_files = []
    mrs_no_files = []

    for i in np.sort(os.listdir(path)):
        
        if os.path.isdir(path + "/"+i):
            print ("Current folder ", (path+"/"+i))
                
            for fname in os.listdir(path + "/"+i):
                print ("fname" , fname)
                if fname.endswith(tuple(f_ext)):
                    next_level = path + "/" + i + "/" + fname 
                    break
                elif fname == "MrSpectroscopy":
                    mrs_level = path + "/" + i + "/" + fname
                    print ("-------------------------------------------------------------------")
                
                    # Check hipp_press_te40_1.rda exists
                    if os.path.isfile(mrs_level +  "/hippo_press_te40_1.rda"):
                        mrs_files.append("hippo_press_te40_1.rda")
                        print ("----- hipp_press_te40_1.rda exists")
                        rda_fname, extension = os.path.splitext("hippo_press_te40_1.rda")
                        dat_file = glob.glob(mrs_level + "/*" + rda_fname + ".dat")
                        for l in dat_file:
                            if os.path.isfile(l):
                                print ("File exits ------" , rda_fname + ".dat")
                                mrs_files.append(rda_fname + ".dat")
                            else:
                                print ("File missing -----", rda_fname + ".dat")
                                mrs_no_files.append(rda_fname + ".dat")
                    else:
                        print ("----hipp_press_te40_1.rda DOES NOT exist---")
                        mrs_no_files.append("hippo_press_te40_1.rda")
                    
                    # Check hipp_press_te40_2.rda exists
                    if os.path.isfile(mrs_level + "/hippo_press_te40_2.rda"):
                        mrs_files.append("hippo_press_te40_2.rda")
                        print ("----- hipp_press_te40_2.rda exists")
                        rda_fname, extension = os.path.splitext("hippo_press_te40_2.rda")
                        dat_file = glob.glob(mrs_level + "/*" + rda_fname + ".dat")
                        for l in dat_file:
                            if os.path.isfile(l):
                                print ("File exits -----" , rda_fname + ".dat")
                                mrs_files.append(rda_fname + ".dat")
                            else:
                                print ("File missing -----", rda_fname + ".dat")
                                mrs_no_files.append(rda_fname + ".dat")
                    else:
                        print ("----hipp_press_te40_2.rda DOES NOT exist-----")
                        mrs_no_files.append("hippo_press_te40_2.rda")
                    
                    # Check hipp_press_te40_ref.rda exists
                    if os.path.isfile(mrs_level + "/hippo_press_te40_ref.rda"):
                        mrs_files.append("hippo_press_te40_ref.rda")
                        print ("----- hipp_press_te40_ref.rda exists")
                        rda_fname, extension = os.path.splitext("hippo_press_te40_ref.rda")
                        dat_file = glob.glob(mrs_level + "/*" + rda_fname + ".dat")
                        for l in dat_file:
                            if os.path.isfile(l):
                                print ("File exits ------" , rda_fname + ".dat")
                                mrs_files.append(rda_fname + ".dat")
                            else:
                                print ("File missing -----", rda_fname + ".dat")
                                mrs_no_files.append(rda_fname + ".dat")
                    else:
                        print ("----hipp_press_te40_ref.rda DOES NOT exist-----")
                        mrs_no_files.append("hippo_press_te40_ref.rda")

                    # check svs_edit .rda file and .dat
                    rda_range = ["1", "2", "3", "ref"]
                    for rda in rda_range:
                        # get the _off.rda file
                        off_file = mrs_level + "/hippo_hx_svs_edit_de2_" + rda + "_off.rda"
                        off_f = "hippo_hx_svs_edit_de2_" + rda + "_off.rda"
                        
                        # get the _on.rda file
                        on_file = mrs_level + "/hippo_hx_svs_edit_de2_" + rda + "_on.rda"
                        on_f = "hippo_hx_svs_edit_de2_" + rda + "_on.rda"
                        
                        # get the .dat file
                        dat_f = glob.glob(mrs_level + "/*_hippo_hx_svs_edit_de2_" + rda + ".dat")

                        # Check _off.rda file
                        if os.path.isfile(off_file):
                            print ("File exits ------" , off_f)
                            mrs_files.append(off_f)
                        else:
                            print ("File missing -----", off_f)
                            mrs_no_files.append(off_f)

                        # Check _on.rda file
                        if os.path.isfile(on_file):
                            print ("File exits ------" , on_f)
                            mrs_files.append(on_f)
                        else:
                            print ("File missing -----", on_f)
                            mrs_no_files.append(on_f)
                            
                        # Check .dat file
                        for l in dat_file:
                            if os.path.isfile(l):
                                print ("File exits ------" , "_hippo_hx_svs_edit_de2_" + rda + ".dat")
                                mrs_files.append("*_hippo_hx_svs_edit_de2_" + rda + ".dat")
                            else:
                                print ("File missing -----", "*_hippo_hx_svs_edit_de2_" + rda + ".dat")
                                mrs_no_files.append("*_hippo_hx_svs_edit_de2_" + rda + ".dat")

                    print ("------------------------------------------------------------")
                    
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
            #print ("Repetition Time  TR ", TR)
            #print ("Echo Time TE ", TE)
            
            # DICOM directory name (long number)
            mapoutname = str(splitup[6])
            print ("folder number", mapoutname)

            print ("+++++++++++++++++++++++++++++++++++++++")
            f.write("%s\t%s\t%s\n" % (filename,int(list_no), i))

            # check the No_of_volumes
            if 'T1w_MPR' in filename:
                if list_no != 416:
                    print ("************ T1w_MPR volumes are missing *****************")
            if 'AdjGre' in filename:
                if list_no != 258:
                    print ("************ AdjGre volumes are missing *****************")
            if 'hx_gre_MT_PKC3_1.5mm' in filename or 'hx_gre' in filename:
                if list_no != 440:
                    print ("************ hx_gre_MT_PKC3_1.5mm volumes are missing *****************")
                    
    f.write("\n\n\n")
    f.write("------  MrSpectroscopy file details --------\n")
    f.write("---------------------------------------------\n\n")
    
    f.write(" following files exist\n")
    f.write("------------------------\n")
    for item in mrs_files:
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write(" following files are missing \n")
    f.write("-----------------------------\n")
    for item in mrs_no_files:
        f.write("%s\n" %(item))

    f.close()
    return 

if __name__ == "__main__":
   #  Please provide the path to the data directory
   path = sys.argv[1]
   
   # Extract files/folders information
   income_data_extract(path)
