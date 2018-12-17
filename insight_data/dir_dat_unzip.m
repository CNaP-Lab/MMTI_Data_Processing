% Directory_data_unzip
%path='/mnt/hcp01/SM_insight_data'
%s=dir(path);
%isusb=[s(:).isdir];
%nameF={s(isusb).name};
%for i = nameF
% end
path='/mnt/hcp01/Insight_data/Insight_data'
cd(path)
s=dir(path);
isusb=[s(:).isdir];
nameF={s(isusb).name};

folderContents = dir;
 for k=1:length(folderContents)
       if folderContents(k).isdir
           myFolder = fullfile(path,folderContents(k).name );
           fprintf('%s\n',myFolder); % or perform task
           cd(myFolder)
           pwd
           gunzip('*.gz')
           delete('*gz')
           cd ..
       end
  end
