#!/bin/bash 

#set the number of nodes and processes per node and wallclock time
#PBS -l nodes=1:ppn=28,walltime=04:00:00

#PBS -q short

# set name of job
#PBS -N meica_50054

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

StudyFolder="/gpfs/projects/MoellerGroup/vat_sud_task/50054"

cd ${StudyFolder}

#meica.py -d "HEAD_FMRI_TASK_1_AP_0053_Head_fMRI_Task_1_AP_20180814100606_53_e1.nii,HEAD_FMRI_TASK_1_AP_0053_Head_fMRI_Task_1_AP_20180814100606_53_e2.nii,HEAD_FMRI_TASK_1_AP_0053_Head_fMRI_Task_1_AP_20180814100606_53_e3.nii" -e 9.24,27.51,45.78 --daw=5 -b 15s 50054_3T_T1w_MPR1.nii.gz --MNI --prefix DCHOICE_fMRI_1

parallel --jobs 4 < 50054_Dechoice_meica.txt
