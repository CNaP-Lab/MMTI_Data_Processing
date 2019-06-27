function y=slc_CorrFix(sub_num, MB)

% This function will call slcCorrFixFull function in (/mnt/jxvs01/tools/matlab_path/Tipp_codes/Trunk/matlab_work). I need to provide multiband factor (mostly 6), 
% data_path (example /mnt/hcp01/tnfcs_mini/1491/unprocessed/3T) then fn : 
% The filename is the name of the functional volume you’re running it on (you will probably want to script a loop that calls all the filenames one after another).

addpath(genpath('/mnt/jxvs01/tools/matlab_path/spm12'))
addpath(genpath('/mnt/jxvs01/tools/matlab_path/Tipp_codes/tipp_help'))
addpath(genpath('/mnt/jxvs01/tools/matlab_path/Tipp_codes/Trunk'))

% cd to save the data - give the path
data_path = sprintf('/mnt/hcp01/tnfcs_mini/%s/unprocessed/3T/', int2str(sub_num))
cd(data_path)

f_List = dir('*fMRI*');

for i=1:length(f_List)
    new_d = f_List(i).name;
    cd(new_d)
    f_file = sprintf('%s_3T_%s.nii.gz', int2str(sub_num), new_d)
    gunzip(f_file);
    fn_file = sprintf('%s_3T_%s.nii', int2str(sub_num), new_d)
    slcCorrFixFULL(fn_file, MB);
    gzip('z*.nii')
    cd ..
end

%for fn= 1:length(fn)
%	slcCorrFixFULL(fn,MB)	
%end
%Obj.update
