from __future__ import print_function
import os, time, string
import dicom
import sys
import numpy as np
import shutil
import glob
# from folders_and_study_RDoC_D import income_data_extract_D
# from folders_and_study_RDoC_C import income_data_extract_C

"""
       Developed By Sameera K. Abeykoon (April, 2019)
       To check Jodi's RDoC Data  - RDoC_C and RDoC_D
       To extract scans files/folders on RDoC_C_Abi_Dargham
       To extract scans files/folders on RDoC_D_Weinstein
       Then it will create a .csv file with scan folder data
       details and missing files information
"""

def income_data_extract_C(path):
    topdir,tobedone = os.path.split(path)

    # Files can come with different file extension
    # DICOM has .dcm or .IMA
    f_ext = (".dcm", ".IMA", ".ima")

    c_folder = [ ]
    rdoc_filename = "RDoC_C_" + tobedone + "_folder_names.csv"
    f = open(rdoc_filename, "w+")
    f.write(("folder name                 " +"\tNumber of files          " + "\tfilename \n"))
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
        print (" MRS level ", mrs_level)
         # List the .rda and .dat files
        for f_file in os.listdir(mrs_level):
            if f_file.endswith(".rda"):
                rda_files.append(f_file)
            elif f_file.endswith(".dat"):
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
                        print ("---- File exits ------" , rda_fname + ".dat")
                        mrs_files.append(rda_fname + ".dat")
                    else:
                        print ("---- File missing -----", rda_fname + ".dat")
                        mrs_no_files.append(rda_fname + ".dat")
            else:
                print ("---- audctx_press_te40_" + rda + ".rda DOES NOT exist----")
                mrs_no_files.append("audctx_press_te40_" + rda + ".rda")
            print ("------------------------------------------------------------")
    except:
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
    rdoc_output = "/mnt/hcp01/codes/outputs/rdoc_scans/" + rdoc_filename
    shutil.move(rdoc_filename, rdoc_output)
    return 

def income_data_extract_D(path):
    topdir,tobedone = os.path.split(path)
                
    # Files can come with different file extension
    # DICOM has .dcm or .IMA
    f_ext = (".dcm", ".IMA", ".ima")

    c_folder = [ ]
    rdoc_filename = "RDoC_D_" + tobedone + "_folder_names.csv"
    f = open(rdoc_filename, "w+")
    f.write(("folder name              " +"\tNumber of files         " + "\tfilename\n"))
    mrs_files = []
    mrs_no_files = []
    rda_files = []
    dat_files = []
    t1w_files = []
    hx_files = []
 
    for i in np.sort(os.listdir(path)):
        
        if os.path.isdir(path + "/"+i):
            # Need to find the MrSpectroscopy folder
            if i == "MrSpectroscopy":
                mrs_level = path + "/" + i
                break
            else:
                for fname in os.listdir(path + "/"+i):
                    if fname == "MrSpectroscopy":
                        mrs_level = path + "/" + i + "/" + fname
                        break
                
            for fname in os.listdir(path + "/"+i):
                print ("fname" , fname)
                if fname.endswith(tuple(f_ext)):
                    next_level = path + "/" + i + "/" + fname 
                    break
    
    # MrSpectroscopy exists
    try:
        print ("MRS level ", mrs_level)
        rda_range = ["1", "2", "ref"]
        for rda in rda_range:
            print ("-------------------------------------------------------------------")
            # Check hippo_press_te40_1.rda , hippo_press_te40_2.rda and 
            # hippo_press_te40_ref files exist
            if os.path.isfile(mrs_level +  "/hippo_press_te40_" + rda + ".rda"):
                mrs_files.append("----- hippo_press_te40_" + rda + ".rda")
                print ("----- hippo_press_te40_" + rda + ".rda exists")
                rda_fname, extension = os.path.splitext("hippo_press_te40_" + rda + ".rda")
                dat_file = glob.glob(mrs_level + "/*" + rda_fname + ".dat")
                for l in dat_file:
                    if os.path.isfile(l):
                        print ("----- File exits ------" , rda_fname + ".dat")
                        mrs_files.append(rda_fname + ".dat")
                    else:
                        print ("----- File missing -----", rda_fname + ".dat")
                        mrs_no_files.append(rda_fname + ".dat")
            else:
                print ("---- hippo_press_te40_" + rda + ".rda DOES NOT exist----")
                mrs_no_files.append("hippo_press_te40_" + rda + ".rda")

        # check svs_edit .rda file and .dat
        svs_range = ["1", "2", "3", "ref"]
        for rda in svs_range:
            # get the _off.rda file
            off_file = mrs_level + "/hippo_hx_svs_edit_de2_" + rda + "_off.rda"
            off_f = "hippo_hx_svs_edit_de2_" + rda + "_off.rda"
                        
            # get the _on.rda file
            on_file = mrs_level + "/hippo_hx_svs_edit_de2_" + rda + "_on.rda"
            on_f = "hippo_hx_svs_edit_de2_" + rda + "_on.rda"
                        
            # get the .dat file
            dat_file = glob.glob(mrs_level + "/*_hippo_hx_svs_edit_de2_" + rda + ".dat")

            # Check _off.rda file
            if os.path.isfile(off_file):
                print ("----- File exits ------" , off_f)
                mrs_files.append(off_f)
            else:
                print ("----- File missing -----", off_f)
                mrs_no_files.append(off_f)

            # Check _on.rda file
            if os.path.isfile(on_file):
                print ("----- File exits ------" , on_f)
                mrs_files.append(on_f)
            else:
                print ("----- File missing -----", on_f)
                mrs_no_files.append(on_f)
                            
            # Check .dat file
            for l in dat_file:
                if os.path.isfile(l):
                    print ("---- File exits ------" , "_hippo_hx_svs_edit_de2_" + rda + ".dat")
                    mrs_files.append("*_hippo_hx_svs_edit_de2_" + rda + ".dat")
                else:
                    print ("---- File missing -----", "*_hippo_hx_svs_edit_de2_" + rda + ".dat")
                    mrs_no_files.append("*_hippo_hx_svs_edit_de2_" + rda + ".dat")

            print ("------------------------------------------------------------")
        
        # List the .rda and .dat files
        for f_file in os.listdir(mrs_level):
            if f_file.endswith(".rda"):
                rda_files.append(f_file)
            elif f_file.endswith(".dat"):
                dat_files.append(f_file)

    except:
        mrs_no_files.append("MrSpectroscopy Folder missing")

    for i in np.sort(os.listdir(path)):
        
        if os.path.isdir(path + "/"+i):
                
            for fname in os.listdir(path + "/"+i):
                if fname.endswith(tuple(f_ext)):
                    next_level = path + "/" + i + "/" + fname 
                    break
            
            try:
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
                    if list_no != 416:
                        print ("************ T1w_MPR volumes are missing *****************")
                        t1w_files.append(" T1w_MPR volumes are missing ")
                if 'AdjGre' in filename:
                    t1w_files.append(filename)
                    if list_no != 258:
                        print ("************ AdjGre volumes are missing *****************")
                        t1w_files.append(" AdjGre - B0 fielmaps volumes are missing ")
                if 'hx_gre_MT_PKC3_1.5mm' in filename or 'hx_gre' in filename:
                    hx_files.append(filename)
                    if list_no != 440:
                        print ("************ hx_gre_MT_PKC3_1.5mm volumes are missing *****************")
                        hx_files.append(" hx_gre_MT_PKC3_1.5mm volumes are missing ")
            except:
                print (" Other Folders - fMRI T1w are  missing ")
                mrs_no_files.append(" Other Folders - fMRI T1w are  missing") 

    f.write("\n\n\n")
    f.write("------ Neuromelanin file Details ------------\n")
    f.write("---------------------------------------------\n\n")
    
    f.write("---- following *hx* files exist -----\n")
    f.write("-------------------------------------\n")
    for item in np.sort(hx_files):
        f.write("%s\n" %(item))

    f.write("\n\n\n")
    f.write("------ T1w and B0 fieldtymaps file details ---------\n")
    f.write("-------------------------------------------------\n\n")
    
    f.write("---- following files exist -------\n")
    f.write("----------------------------------\n")
    for item in np.sort(t1w_files):
        f.write("%s\n" %(item))
                     
    f.write("\n\n\n")
    f.write("------ MrSpectroscopy file details --------\n")
    f.write("---------------------------------------------\n\n")
    
    f.write("---- following files exist --------\n")
    f.write("-----------------------------------\n")
    for item in np.sort(mrs_files):
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write("---- following files are missing ------\n")
    f.write("---------------------------------------\n")
    for item in np.sort(mrs_no_files):
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write(" ----- following *.rda* files exist -----------\n")
    f.write("-----------------------------------------------\n")
    for item in np.sort(rda_files):
        f.write("%s\n" %(item))

    f.write("\n\n")
    f.write("---- following *.dat* files exist ----\n")
    f.write("--------------------------------------\n")
    for item in np.sort(dat_files):
        f.write("%s\n" %(item))

    f.close()
    rdoc_output = "/mnt/hcp01/codes/outputs/rdoc_scans/" + rdoc_filename
    shutil.move(rdoc_filename, rdoc_output)
    return 


if __name__ == "__main__":
   #  Please provide the path to the data directory
   # path = sys.argv[1]
   path = raw_input("Enter input data path ? example:/mnt/jxvs01/incoming/RDoC_C_Abi_Dargham/S3927_V126_AAD ? :")

   topdir,tobedone = os.path.split(path)
   print ("Incoming data directory path", topdir)   
   print ("Subject data directory ", tobedone)

   top_path, rdoc = os.path.split(topdir)

   if rdoc == "RDoC_C_Abi_Dargham":
       income_data_extract_C(path)
   elif rdoc == "RDoC_D_Weinstein":
       income_data_extract_D(path)
   else:
       print ("This is not RDoC_C or RDoC_D data scan")
    
