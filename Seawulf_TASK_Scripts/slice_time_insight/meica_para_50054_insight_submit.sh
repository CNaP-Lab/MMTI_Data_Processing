#!/bin/bash 

#set the number of nodes and processes per node and wallclock time
#PBS -l nodes=1:ppn=28,walltime=04:00:00

#PBS -q short

# set name of job
#PBS -N meica_Ins_50054

# mail alert at (b)eginning, (e)nd and (a)bortion of execution
#PBS -m bea

# send mail to the following address
#PBS -M sameera.abeykoon@stonybrookmedicine.edu

# use submission environment 
#PBS -V

# start job from the directory it was submitted (see following)
cd $PBS_O_WORKDIR
# cd /gpfs/projects/MoellerGroup/TASK_scripts 

module load shared
module load gsl/2.4.0
module load afni/17.2.05
module load anaconda/2 
module load gnu-parallel/6.0

StudyFolder="/gpfs/projects/MoellerGroup/Insight_task/50054"

cd ${StudyFolder}

parallel --jobs 2 < 50054_Insight_meica.txt
#meica.py -d "1.3.12.2.1107.5.2.43.67057.2018110517051173143186610.0.0.0_fMRI_Metacog_AP_1_20181105155313_18.nii,1.3.12.2.1107.5.2.43.67057.2018110517051173143186610.0.0.0_fMRI_Metacog_AP_1_20181105155313_18_e2.nii,1.3.12.2.1107.5.2.43.67057.2018110517051173143186610.0.0.0_fMRI_Metacog_AP_1_20181105155313_18_e3.nii" -e 6.4,16.86,27.32 --daw=5 -b 15s T1w.nii --MNI --tpattern=@/gpfs/projects/MoellerGroup/Metacog/50028/filename.txt --prefix Metacog_fMRI_1
