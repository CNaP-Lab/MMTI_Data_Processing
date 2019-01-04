import numpy as np
import pylab as P
import pandas
import os
import glob
import sys
#%matplotlib inline

def parsedei(indei):
    import pandas
    colnames="onset rawStim rawRT   trial   SOA     RT      category        scoring resp    scored  prompt".split()
    rawtypes=['f16']*6 + ['S128']*2 + ['f16']*2 + ['S128']
    coltypes = zip(colnames,rawtypes)
    dei = np.genfromtxt(indei,comments='#',delimiter='\t',dtype=coltypes)
    print dei[0]
    return pandas.DataFrame(dei)

def regname(indei):
    return dict(zip(['subid','rnum'],''.join(os.path.basename(indei).split('.')[:-1]).split('-')[1:3]))

taskname="Insight"
subid = sys.argv[1]

if len(sys.argv) > 2:
	fmri = sys.argv[2:]
else:
	fmri = [f for f in glob.glob("*_medn.nii.gz")]

# deidir="/home/prantik/data/Scott_Bachi/Jan-2018/behavioral/"
# Provide the Insight behavioral files
deidir = "/gpfs/projects/MoellerGroup/Insight_task/behavioral"
globstr = '%s/*-%s-*.dei' % (deidir, subid)
deifiles = sorted(glob.glob(globstr))

if len(deifiles)==0:
	print "No behavioral files found. Exiting."
	sys.exit()

for runid in range(len(deifiles)):
    indei = deifiles[runid]
    fninfo = regname(indei)
    dei = parsedei(indei)
    dei.ix[np.isnan(dei.ix[:,'RT']),'RT']=7500
    categs = np.unique(dei.ix[:,'category'])
    dei.ix[:,'rawStim']=dei.ix[:,'rawStim']/1000
    dei.ix[:,'RT']=dei.ix[:,'RT']/1000
    stevstrs=[]
    for cc in categs:
        outname = 'S%s_%s_%s.1D' % (fninfo['subid'],cc,taskname)
        if runid==0 : ofh = open(outname,'w')
        else: 
            ofh = open(outname,'a')
            ofh.write('\n')
        rawStims = dei.ix[dei.ix[:,'category']==cc,'rawStim']
        rawRTs = dei.ix[dei.ix[:,'category']==cc,'RT']
        stevs = zip(rawStims,rawRTs)
        stevstr = ' '.join([':'.join([str(ss) for ss in stev]) for stev in stevs]) 
        ofh.write( stevstr )
        ofh.close()

deconstimtxt = ["3dDeconvolve -overwrite -tout -xout -fout -cbucket S%s_Insight_cbk -prefix S%s_Insight -input %s -num_stimts %i -x1D Insight.xmat.1D -polort 2 -gltsym 'SYM: +drugSelf +foodSelf -drugOther -foodOther' -glt_label 1 self_v_other -gltsym 'SYM: +drugSelf +drugOther -foodSelf -foodOther' -glt_label 2 drug_v_food -gltsym 'SYM: +drugSelf -foodSelf -drugOther +foodOther' -glt_label 3 interaction" % (subid, subid,' '.join(fmri), len(categs)) ]
for cc_ii in range(len(categs)):
	cc = categs[cc_ii]
	outname = 'S%s_%s_%s.1D' % (fninfo['subid'],cc,taskname)
	deconstimtxt.append("-stim_label %i %s "  % (cc_ii+1,cc) )
	deconstimtxt.append("-stim_times_AM1 %i %s 'dmBLOCK(1)' "  % (cc_ii+1,outname) )
deconstimtxt.append("; 3drefit -view tlrc S%s_%s+orig; 3drefit -view tlrc S%s_%s_cbk+orig  "  % (subid,taskname,subid,taskname) )
os.system(" ".join(deconstimtxt))

print ' '.join(deconstimtxt)
