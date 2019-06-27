function y=tipp_qc(data_path,qc_path)

%addpath(genpath('/gpfs/software/spm/12'))
%addpath(genpath('/gpfs/projects/VanSnellenbergGroup/matlab_tipp'))
addpath(genpath('/mnt/jxvs01/tools/matlab_path/spm12'))
addpath(genpath('/mnt/jxvs01/tools/matlab_path/Tipp_codes/tipp_help'))
addpath(genpath('/mnt/jxvs01/tools/matlab_path/Tipp_codes/Trunk'))

% cd to save the data - to the /mnt/jxvs01/imaging_data folder
cd(qc_path)

Obj=TIPPstudy(data_path, 'initln')
Obj.update
