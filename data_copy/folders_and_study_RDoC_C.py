from __future__ import print_function
import os, time, string
import dicom
import sys
import numpy as np
import glob

#################################################################################
#                                                                               #
#                       Developed By Sameera K. Abeykoon (April, 2019)          #
#                       To extract scans files/folders on RDoC_C_Abi_Dargham    #
#                                                                               #
#################################################################################


def income_data_extract_C(path):
    topdir,tobedone = os.path.split(path)
    print ("Incoming data directory path", topdir)   
    print ("Subject data directory ", tobedone)

    # Files can come with different file extension
    # DICOM has .dcm or .IMA
    f_ext = (".dcm", ".IMA", ".ima")

    c_folder = [ ]
    f = open("RDoC_C_" + tobedone + "_folder_names.csv","w+")
    f.write(("folder name" +"\tNumber of files" + "\tfilename \n"))
    mrs_files = []
    mrs_no_files = []
    rda_files = []
    dat_files = []
    t1w_files = []
    hx_files = []

    for i in np.sort(os.listdir(path)):
        
        if os.path.isdir(path + "/"+i):
            # print ("Current folder ", (path+"/"+i))
            
            if i == "MrSpectroscopy":
                mrs_level = path + "/" + i
                break
            else:
                for fname in os.listdir(path + "/"+i):
                    if fname == "MrSpectroscopy":
                        mrs_level = path + "/" + i + "/" + fname
                        break
    try:
        print ("MRS level ", mrs_level)
         # List the .rda and .dat files
        for f_file in os.listdir(mrs_level):
            if f_file.endswith(".rda"):
                rda_files.append(f_file)
            elif f_file.endswith(".dat"):
                print ("dat file : ", f_file)
                dat_files.append(f_file)

        rda_range = ["1", "2", "ref"]
        for rda in rda_range:
            print ("-------------------------------------------------------------------")
            # Check audctx_press_te40_1.rda ,audctx_press_te40_2.rda and 
            # audctx_press_te40_ref files exist
            if os.path.isfile(mrs_level +  "/audctx_press_te40_" + rda + ".rda"):
                mrs_files.append("audctx_press_te40_" + rda + ".rda")
                print ("----- audctx_press_te40_" + rda + ".rda exists")
                rda_fname, extension = os.path.splitext("audctx_press_te40_" + rda + ".rda")
                dat_file = glob.glob(mrs_level + "/*" + rda_fname + ".dat")
                for l in dat_file:
                    if os.path.isfile(l):
                        print ("File exits ------" , rda_fname + ".dat")
                        mrs_files.append(rda_fname + ".dat")
                    else:
                        print ("File missing -----", rda_fname + ".dat")
                        mrs_no_files.append(rda_fname + ".dat")
            else:
                print ("----audctx_press_te40_" + rda + ".rda DOES NOT exist----")
                mrs_no_files.append("audctx_press_te40_" + rda + ".rda")
            print ("------------------------------------------------------------")
    except:
        print ("MrSpectroscopy Folder missing")
        mrs_no_files.append("MrSpectroscopy Folder missing")


    for i in np.sort(os.listdir(path)):
        
        if os.path.isdir(path + "/"+i):
                
            for fname in os.listdir(path + "/"+i):
                if fname.endswith(tuple(f_ext)):
                    next_level = path + "/" + i + "/" + fname 
                    break

            splitup = next_level.split('/')
            
            list_no = len(os.listdir(path + "/" + i))

            dcmhdr = dicom.read_file(next_level)
            filenum = int(dcmhdr['0020','0011'].value)
            filename = dcmhdr['0008','103e'].value
            # TR = dcmhdr['0018', '0080'].value # Repetition Time
            # TE = dcmhdr['0018', '0081'].value # Echo Time
            
            # filename given example: fMRI_Resting_1_AP, T1W_MPR
            c_folder.append(filename)
            
            # DICOM directory name (long number)
            mapoutname = str(splitup[6])

            f.write("%s\t%s\t%s\n" % (i, int(list_no), filename))

            # check the No_of_volumes
            if 'T1w_MPR' in filename:
                t1w_files.append(filename)
                if list_no == 416:
                    print ("************ All T1w_MPR volumes are there *****************")
                elif list_no == 417:
                    print ("************ All T1w_MPR volumes are there *****************")
                else:
                    print ("************ T1w_MPR volumes are missing *****************")
                    t1w_files.append(" T1w_MPR volumes are missing ")
            if 'AdjGre' in filename:
                t1w_files.append(filename)
                if list_no != 258:
                    print ("************ AdjGre volumes are missing *****************")
                    t1w_files.append(" AdjGre - B0 fielmaps volumes are missing ")
            if 'hx_gre_MT_PKC3_1.5mm' in filename or 'hx_gre' in filename:
                hx_files.append(filename)
                if list_no != 200:
                    print ("************ hx_gre_MT_PKC3_1.5mm volumes are missing *****************")
                    hx_files.append(" hx_gre_MT_PKC3_1.5mm volumes are missing ")
    
    f.write("\n\n\n")
    f.write("------ Neuromelanin file Details ------------\n")
    f.write("---------------------------------------------\n\n")
    
    f.write("---- following *hx* files exist ------\n")
    f.write("--------------------------------------\n")
    for item in np.sort(hx_files):
        f.write("%s\n" %(item))

    f.write("\n\n\n")
    f.write("------ T1w and B0 fieldmaps file details --------\n")
    f.write("------------------------------------------------\n\n")
    
    f.write("---- following files exist -------\n")
    f.write("----------------------------------\n")
    for item in np.sort(t1w_files):
        f.write("%s\n" %(item))

    f.write("\n\n\n")
    f.write("------  MrSpectroscopy file details ---------\n")
    f.write("---------------------------------------------\n\n")
    
    f.write("---- following files exist ------\n")
    f.write("---------------------------------\n")
    for item in mrs_files:
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write("---- following files are missing ----\n")
    f.write("-------------------------------------\n")
    for item in mrs_no_files:
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write("--- following *.rda* files exist ----\n")
    f.write("-------------------------------------\n")
    for item in np.sort(rda_files):
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write("--- following *.dat* files exist ---\n")
    f.write("------------------------------------\n")
    for item in np.sort(dat_files):
        f.write("%s\n" %(item))

    f.close()
    return 

if __name__ == "__main__":
   #  Please provide the path to the data directory
   path = sys.argv[1]
   
   # Extract files/folders information
   income_data_extract_C(path)
