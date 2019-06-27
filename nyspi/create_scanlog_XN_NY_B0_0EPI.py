from __future__ import print_function
import os, time, string
import sys
from subprocess import call
import dicom

#Modify this:

#topdir = "/mnt/jxvs01/incoming/NYSPI_data/XNAT_K01/horgconte"
#tobedone = ['3012']

#  Please provide the path to the data directory
# example: ipython create_scanlog_SB.py /mnt/jxvs01/incoming/JVS_K01_VanSnellenberg/S3046_V26_JV

# topdir=/mnt/jxvs01/incoming/JVS_K01_VanSnellenberg
# tobedone=S3046_V26_JV

# create_scanlog_XN_NY_B0_0EPI.py - 0=PA,  50000=AP

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

m = 0
n = 0
p = 0
q = 0
e = 0

# Files can come with different file extension
# DICOM has .dcm or .IMA
f_ext = (".dcm", "IMA")

while os.path.isdir(current_dir):
    breakout = 0
    for i in os.listdir(current_dir):

        if current_dir == topdir and i not in tobedone:
            continue
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

            splitup = next_level.split('/')[1:]

            dcmhdr = dicom.read_file(next_level)
            filenum = int(dcmhdr['0020','0011'].value)
            filename = dcmhdr['0008','103e'].value
            
            print (filename)            
            
            #studyname = str(splitup[5])
            #mapoutname = str(splitup[5]) + '_' + str(splitup[6])
            #snum = str(splitup[6]) + '/scans/' + str(splitup[8])

            studyname = str(splitup[6])
            mapoutname = str(splitup[6]) + '_' + str(splitup[7])
            snum = str(splitup[7]) + '/scans/' + str(splitup[9])+'/DICOM'
            
            print (studyname)
            print (mapoutname)
            print ("snum", snum)

            if studyname not in allstudy:
                allstudy.append(studyname)
                allstring.append([])

            if mapoutname not in mapoutlist:
                mapoutlist.append(mapoutname)
                mapoutcont.append([])
                mapouttype.append([])
                mapoutlabel.append([])
                mapoutsnum.append([])
                mapoutextra.append([])

            mapindex = mapoutlist.index(mapoutname)

            if 'TOPUP_FPE' in filename:
                
                a = float(dcmhdr['0043','102c'].value)/1000000
                b = filename.split(' ')
                c = "%.6f" % (a)
                d = (dcmhdr['0019', '107d'].value)
                print ("d", d)

                mapoutcont[mapindex].append(filenum)
                #if d == 0:
                print ("Topup_PA", d)
                mapouttype[mapindex].append('Topup_PA')
                #else:
                #   mapouttype[mapindex].append('Topup_AP')
                mapoutlabel[mapindex].append('_'.join(b))
                mapoutsnum[mapindex].append(snum)
                mapoutextra[mapindex].append(c)
                                                
            elif 'TOPUP_RPE' in filename:

                a = float(dcmhdr['0043','102c'].value)/1000000
                b = filename.split(' ')
                c = "%.6f" % (a)
                d = (dcmhdr['0019', '107d'].value)
                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('Topup_AP')
                mapoutlabel[mapindex].append('_'.join(b))
                mapoutsnum[mapindex].append(snum)
                mapoutextra[mapindex].append(c)

            elif 'MAP B0' in filename:

                a = filename.split(' ')
                d = (dcmhdr['0019', '107d'].value)

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('B0_fieldmap')
                mapoutlabel[mapindex].append('_'.join(a))
                mapoutsnum[mapindex].append(snum)
                #mapoutsnum[mapindex].append(0)
                mapoutextra[mapindex].append(0)
        
            elif 'STRUC T2CUBE SAG3D ARC .8' in filename:

                a = float(dcmhdr['0018','0095'].value)
                aa= float(dcmhdr['0028','0010'].value)
                b = filename.split(' ')
                #c = "%.6f %.6f" % (a,aa)
                c = str(1/(a*aa))

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('T2w_SPC_')
                mapoutlabel[mapindex].append('_'.join(b))
                mapoutsnum[mapindex].append(snum)
                mapoutextra[mapindex].append(c)

            elif 'STRUC BRAVO SAG3D ARC .8' in filename:

                a = float(dcmhdr['0018','0095'].value)
                aa= float(dcmhdr['0028','0010'].value)
                b = filename.split(' ')
                #c = "%.6f %.6f" % (a,aa)
                c = str(1/(a*aa))

                mapoutcont[mapindex].append(filenum)
                mapouttype[mapindex].append('T1w_MPR_')
                mapoutlabel[mapindex].append('_'.join(b))
                mapoutsnum[mapindex].append(snum)
                mapoutextra[mapindex].append(c)

            elif 'FUNC' in filename and 'TOPUP' not in filename:

                a = filename.split(' ')
                d = (dcmhdr['0019', '107d'].value)
                print ("d", d)

                if 'CTA' in filename:
                    m += 1
                    e = m
                elif 'SOT' in filename:
                    n += 1
                    e = n
                elif 'RS' in filename:
                    p += 1
                    e = p
                elif 'TL' in filename:
                    q += 1
                    e = q

                if d == 0:
                   mapouttype[mapindex].append('fMRI_'+ a[2] + '_' + str(e) +  '_PA')
                else:
                   mapouttype[mapindex].append('fMRI_'+ a[2] + '_' + str(e) + '_AP')

                mapoutcont[mapindex].append(filenum) 
                #mapouttype[mapindex].append('fMRI_'+ a[2] + '_')
                mapoutlabel[mapindex].append('_'.join(a))
                mapoutsnum[mapindex].append(snum)
                mapoutextra[mapindex].append(0)
                  
            break

    if breakout:
        continue

    alldir.append(current_dir)

    if current_dir == topdir:
        break
    else:
        current_dir = topdir

for i in range(len(mapoutlist)):
    p = [x for (y,x) in sorted(zip(mapoutcont[i], mapoutextra[i]))]
    q = [x for (y,x) in sorted(zip(mapoutcont[i], mapouttype[i]))]
    r = [x for (y,x) in sorted(zip(mapoutcont[i], mapoutlabel[i]))]
    s = [x for (y,x) in sorted(zip(mapoutcont[i], mapoutsnum[i]))]
    mapoutcont[i].sort()
    print ("p", p)
    print ("q", q)
    print ("r", r)
    print ("s", s)
    
    previousapecho = 0
    previouspaecho = 0
    previousb0echo = 0

    whichstudy = str(mapoutlist[i]).split('_')[0]
    print ("which study", whichstudy)
    
    for j in range(len(mapoutcont[i])):
        if 'Topup_AP' in  q[j] and not previousapecho:
            allap.append(whichstudy + '_'+ q[j])            
            previousapecho = allap.count(whichstudy +'_'+ q[j])
            apscanfirst = 1
            continue

        if 'Topup_PA' in  q[j] and not previouspaecho:
            allpa.append(whichstudy +'_'+ q[j])
            previouspaecho = allpa.count(whichstudy +'_'+ q[j])
            pascanfirst = 1
            continue

        if 'B0_fieldmap' in  q[j] and not previousb0echo:
            allb0.append(whichstudy +'_'+ q[j])
            previousb0echo = allb0.count(whichstudy +'_'+ q[j])
            b0scanfirst = 1
            continue

    for j in range(len(mapoutcont[i])):
        if 'Topup_AP' in  q[j]:
            if apscanfirst:
                apscanfirst = 0
            else:
                allap.append(whichstudy +'_'+ q[j])

            previousapecho = allap.count(whichstudy +'_'+ q[j])

            allstring[allstudy.index(whichstudy)].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + q[j] + ' ' + str(previousapecho) + ' 2 ' + p[j])
            
        if 'Topup_PA' in  q[j]:
            if pascanfirst:
                pascanfirst = 0
            else:
                allpa.append(whichstudy +'_'+ q[j])

            previouspaecho = allpa.count(whichstudy +'_'+ q[j])

            allstring[allstudy.index(whichstudy)].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + q[j] + ' ' + str(previouspaecho) + ' 1 ' + p[j])

        if 'B0_fieldmap' in  q[j]:
            if b0scanfirst:
                b0scanfirst = 0
            else:
                allb0.append(whichstudy +'_'+ q[j])

            previousb0echo = allb0.count(whichstudy +'_'+ q[j])

            allstring[allstudy.index(whichstudy)].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + q[j] + ' ' + str(previousb0echo) + ' ' + '0' + ' ' + '0')
            
        if 'T1w_MPR_' in  q[j]:
            allt1.append(whichstudy +'_'+ q[j])
            o = float(allt1.count(str(mapoutlist[i]) +'_'+ q[j]))/2
            if o.is_integer():
                n = q[j] + str(allt1.count(whichstudy +'_'+ q[j]))

                allstring[allstudy.index(whichstudy)].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + n + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' ' + p[j])

        if 'T2w_SPC_' in  q[j]:
            allt2.append(whichstudy +'_'+ q[j])
            o = float(allt1.count(str(mapoutlist[i]) +'_'+ q[j]))/2
            if o.is_integer():
                n = q[j] + str(allt2.count(whichstudy +'_'+ q[j]))

                allstring[allstudy.index(whichstudy)].append(' ' + str(s[j]) + ' 12:00 ' +  str(r[j]) + ' ' + n + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' ' + p[j])

        if 'fMRI' in q[j]:
            allfunc.append(whichstudy +'_'+ q[j])

            #h = int(allfunc.count(whichstudy +'_'+ q[j]))

            #if h%2:
            t = q[j].split('_')
            if t.pop() == 'PA':
                #allstring[allstudy.index(whichstudy)].append(' ' + s[j] + ' 12:00 ' +  str(r[j]) + ' ' + q[j] + str(1) + ' ' + str(previouspaecho) + ' ' + str(previousb0echo) + ' 1')
                allstring[allstudy.index(whichstudy)].append(' ' + s[j] + ' 12:00 ' +  str(r[j]) + ' ' + '_'.join(t)  + ' '+  str(previouspaecho) + ' ' + str(previousb0echo) + ' 1')
            else:
                allstring[allstudy.index(whichstudy)].append(' ' + s[j] + ' 12:00 ' +  str(r[j]) + ' ' + '_'.join(t) + ' ' + str(previousapecho) + ' ' + str(previousb0echo) + ' 2')


for i in range(len(allstudy)):
    f = open(str(allstudy[i]) + '_scanlog_B0EPI0.txt','w')
    k = 0
    for j in allstring[i]:
        k = k + 1
        f.write(str(k)+j+'\n')
    f.close()
