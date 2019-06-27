"""
	Developed By: Sameera Abeykoon 
        Feb 2019
        Use python 2.7

"""
 
from __future__ import print_function, division
import os, time, string
import sys
import numpy as np
import re
import pandas as pd

num_list = []
#txtfile = raw_input("Please enter the .txt file ? " )
txtfile = "/mnt/hcp01/insight_task/Insight_task/InsightExample/13015-1.txt"

base = os.path.basename(txtfile)
sub_num = os.path.splitext(base)[0]

scoring = []
RT = []
rawRT = []
rawStim = []
t_prompt = []
category = []
start = []
resp = []
add_level = []
level = 0

with open(txtfile, 'r') as infile:
    lines = infile.readlines()
    
    # First get the information from header
    copy = False
    for i, line in enumerate(lines):
        # Copy the heder file information
        if "Experiment" in line:
            copy = True
        if "DataFile.Basename" in line:
                copy = False
        if copy:
            start.append("# " + line)
        # Extract the Onset start value
        if "msInstruct" in line:
            ms_Ins = (line.split(":"))[-1]
            print (ms_Ins)
        # Extract the Onset append value
        if "msStim" in line:
            ms_stim = (line.split(":"))[-1]
            print (ms_stim)
        # If the Header file details end break this loop
        if "Header End" in line:
            break 

        
    header_end = False            
    for i, line in enumerate(lines):
        if "Header End" in line:
            header_end = True
        if header_end:
            if "scoring" in line:
                result = line.split(": ")
                re1 = (result[-1]).rstrip()
                scoring.append(re1)
            elif "category" in line:
                result = (line.split(": "))
                re1 = (result[-1]).rstrip()
                category.append(re1)
            elif "thoughtPrompt" in line:
                result = line.split(": ")
                # to remove trailing space
                re1 = (result[-1]).strip() 
                t_prompt.append("\""+ re1 + "\"")
            elif "textStimulus.RTTime" in line:
                result = line.split(": ")
                rawRT.append(result[-1])
            elif "textStimulus.RT" in line:
                result = line.split(": ")
                RT.append(result[-1])
            elif "textStimulus.OnsetTime" in line:
                result = line.split(": ")
                rawStim.append(result[-1])
            elif  "textStimulus.RESP" in line:
                resp.append((line.split(": "))[-1])
            elif "Level: 2" in line:
                add_level.append(level)
                level = 0
            elif "Level: 3" in line:
                level += 1
                
                
RTTotal = 0
# Save the data into new file
dei_file = sub_num + ".dei"
with open(dei_file, 'w') as file:
    for i in start:
        file.write(i)
    
    file.write("# data source: -	('-' indicates streamed values- no intermediary file) \n")
    file.write("# \n")
    file.write("# Variable names are in the next line: -------------- \n")
    file.write("# onset  rawStim rawRT trial  SOA  RT  category  scoring resp scored prompt \n")
    score = 0
    trial = 6
    onset = 0
    
    ds_resp = 0
    ds_RT = 0
    ds = 0
    do_resp = 0
    do_RT = 0
    do = 0
    fs_resp = 0
    fs_RT = 0
    fs = 0
    fo_resp = 0
    fo_RT = 0
    fo = 0
    
    # interlize category NAN's
    dsNAN = 0
    doNAN = 0
    fsNAN = 0
    foNAN = 0

    #for j in rawStim):
    j = 0
    Onset_val = []
    SOA_val = []
    for k in add_level:
        le = 0
        for kk in range(k):
            if le == 0:
                onset = int(ms_Ins)
                SOA = int(ms_Ins) 
                le = 1
            else:
                SOA = int(rawStim[j]) - int(rawstim_pr)
                onset = onset + int(SOA)
            rawstim_pr = rawStim[j]
            j += 1
            Onset_val.append(onset)
            SOA_val.append(SOA)
            

    for j, value in enumerate(rawStim):
        # getting resp mean and RT total and Mean
        # each Category 
        try:
            resp_u = int(resp[j])
        except ValueError:
            # No reponse give zero
            resp_u = "NAN"
        
        # Change the responses to
        # 8 --> 1 , 7 --> 2, 1 --> 3
        # 2 --> 4, 3 --> 5
        if resp_u == 8:
            n_resp = 1
        elif resp_u == 7:
            n_resp = 2
        elif resp_u == 1:
            n_resp = 3
        elif resp_u == 2:
            n_resp = 4
        elif resp_u == 3:
            n_resp = 5
        else:
            n_resp = "NAN"

        # if scoring is reverse change
        # 1 --> 5, 2 --> 4, 3 --> 3 
        # 4 --> 2, 5 --> 1
        if scoring[j] == "reverse":
            if n_resp == 1:
                score = 5
            elif n_resp == 2:
                score = 4
            elif n_resp == 3:
                score = 3
            elif n_resp == 4:
                score = 2
            elif n_resp == 5:
                score = 1
            elif n_resp == "NAN":
                score = "NAN"
        else:
            score = n_resp
        
        try:
            new_RT = int(RT[j])
            #if scoring[j] == "direct":
            new_resp = int(score)
            #else :
            #    new_resp = 0
            # print (category[j], new_resp, new_RT)
            if (category[j]) == "drugSelf":
                ds_resp = ds_resp +  new_resp
                ds_RT = ds_RT + new_RT 
                ds += 1
            elif (category[j]) == "drugOther":
                do_resp = do_resp + new_resp
                do_RT = do_RT + new_RT
                do += 1
            elif (category[j]) == "foodSelf":
                fs_resp = fs_resp + new_resp
                fs_RT = fs_RT + new_RT
                fs += 1
            elif (category[j]) == "foodOther":
                fo_resp = fo_resp + new_resp
                fo_RT = fo_RT + new_RT
                fo += 1
        except ValueError:
            if (category[j]) == "drugSelf":
                dsNAN += 1
            elif (category[j]) == "drugOther":
                doNAN += 1
            elif (category[j]) == "foodSelf":
                fsNAN += 1
            elif (category[j]) == "foodOther":
                foNAN += 1

        # remove unwanted spaces after the values : need to get the int value
        try:
            value_c = int(value)
        except ValueError:
            value_c = "NAN"
        try:
            rawRT_c = int(rawRT[j])
        except ValueError:
            rawRT_c = "NAN"
        try:
            RT_c = int(RT[j])
        except ValueError:
            RT_c = "NAN"

        if n_resp == "NAN":
            RT_c = "NAN"
            rawRT_c = "NAN"


        file.write(str(Onset_val[j]) + " " +str(value_c) + " " + str(rawRT_c) + " " + str(trial) + " " + str(SOA_val[j]) + " " + str(RT_c) + " " + category[j] + " " + str(scoring[j]) + " " + str(n_resp) + " " + str(score) + " " + t_prompt[j] + "\n")
        trial += 1

        # print "# Waiting for MR sync... when new set starts
        try:
            next_onset = Onset_val[j +1]
            if int(next_onset) == 10000:
                file.write("# Waiting for MR sync... \n")
        except IndexError:
            print ("Done with the list")
     
    # get the mean values for each category
    ds_RTmean = round(ds_RT/ds, 3) if ds != 0 else 0
    do_RTmean = round(do_RT/do, 3) if do != 0 else 0
    fs_RTmean = round(fs_RT/fs, 3) if fs != 0 else 0
    fo_RTmean = round(fo_RT/fo, 3) if fo != 0 else 0

    ds_mean = round(ds_resp/ds, 3) if ds != 0 else 0
    do_mean = round(do_resp/do, 3) if do != 0 else 0
    fs_mean = round(fs_resp/fs, 3) if fs != 0 else 0
    fo_mean = round(fo_resp/fo, 3) if fo != 0 else 0


    file.write("# Waiting for MR sync... \n")
    file.write("## --------------------------------------------------------------------------------------------------- \n")
    file.write("## For trials that had responses ('resps'), r(esponses)Tot(al), r(esponses)Mean, rtTot(al), rtMean \n")
    file.write("## category NaNs resps rMean rtTot rtMean \n")
    print (ds_resp, ds_RT, do_resp, do_RT, fs_resp, fs_RT, fo_resp, fo_RT)
    #print (ds_mean, do_mean, fs_mean, fo_mean)
    print (dsNAN, doNAN, fsNAN, foNAN)
    file.write("## drugSelf " + str(dsNAN) + " " + str(ds) + " " + str(ds_resp) + " " + str(ds_mean) + " " + str(ds_RT) + " "  + str(ds_RTmean) + " " + "\n")
    file.write("## drugOther "+ str(doNAN) + " " + str(do) + " " + str(do_resp) + " " + str(do_mean) + " " +str(do_RT) + " "  + str(do_RTmean) + " " + "\n")
    file.write("## foodSelf " + str(fsNAN) + " " + str(fs) + " " + str(fs_resp) + " " + str(fs_mean) + " " + str(fs_RT) + " "  + str(fs_RTmean) + " " + "\n")
    file.write("## foodOther " + str(foNAN) + " " + str(fo) + " " + str(fo_resp) + " " + str(fo_mean) + " " + str(fo_RT) + " " + str(fo_RTmean) + " " + "\n")
