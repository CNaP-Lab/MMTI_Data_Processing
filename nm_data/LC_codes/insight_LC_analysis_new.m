clear all
close all
root_folder = ['/gpfs/projects/MoellerGroup/NM_data/nm_data/LCdata']

load LC_key_new;
LC_key= x;
%LC_key=LC_key_all(LC_key_all(:,2)==1,:);
%LC_key= LC_key_all(LC_key_all(:,1)==3133,:);

for s=1:length(LC_key(:,1))
    
    s;
    Subjects{s} = num2str(LC_key(s,1))
    %clearvars?
    if LC_key(s,2)==2
        LCmask = spm_read_vols(spm_vol([root_folder '/LC subjects/LC' Subjects{s} '.nii']));
        v=spm_vol([root_folder '/LC subjects/complete/NM' Subjects{s} '.nii']);
        NMimage = spm_read_vols(v);
    elseif LC_key(s,2)==1
        LCmask = spm_read_vols(spm_vol([root_folder '/LC subjects/LC' Subjects{s} 'nac.nii']));
        v=spm_vol([root_folder '/LC subjects/complete/NM' Subjects{s} 'nac.nii']);
        NMimage = spm_read_vols(v);
    elseif LC_key(s,2)==3
        LCmask = spm_read_vols(spm_vol([root_folder '/LC subjects/cocaine/LC' Subjects{s} '.nii']));
        v=spm_vol([root_folder '/LC subjects/cocaine/NM' Subjects{s} '.nii']);
        NMimage = spm_read_vols(v);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    elseif LC_key(s,2)==4
        LCmask = spm_read_vols(spm_vol([root_folder '/LCnewbin' Subjects{s} '.nii']));
        v=spm_vol([root_folder '/NM' Subjects{s} '.nii']);
        NMimage = spm_read_vols(v);
    end
%LCvoxels(:,s) = NMimage(LCmask==1);
LCvoxels(:,s) = NMimage(LCmask>=1);
for i =1:size(LCvoxels,1)
    for j = 1:size(LCvoxels,2)
 LCvoxels_Z(i,j) = (LCvoxels(i,j)-mean(LCvoxels(:,j)))/std(LCvoxels(:,j));
    end
end
LCvoxels(LCvoxels_Z<-1.5)=NaN;
LCsignal = nanmean(LCvoxels);
LCsignal_orig(s) = mean(NMimage(LCmask==1));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%try downweigting outlier voxels
for k=1:size(LCmask,3)
    has_mask0=sum(LCmask(:,:,k));
    has_mask1(k)=sum(has_mask0);
end

has_mask2=find(has_mask1>0);

NMimage2D = NMimage(:,:,has_mask2);
LCmask2D = LCmask(:,:,has_mask2);

    column_sum = sum(LCmask2D);
%     if max(column_sum)<4
%         need_rotation(s,1) = 1;
%     else 
%         need_rotation(s,1) = 0;
%     end
   
        for d = 1:41
            
            image_test = imrotate(LCmask2D,d-21);
            column_sum2= sum(image_test);
            max_column(d) = max(column_sum2);
            
        end
        best_angles2{s} = find(max_column==6)-21;
        best_angles = find(max_column==6)-21;
        if find(best_angles==0)>0;
            best_angle(s) = 0;
        elseif max(best_angles)<0
        best_angle(s) = max(best_angles);
        elseif min(best_angles)>0
            best_angle(s) = min(best_angles);        
        end
        %%%%%%%%%%%%%%%%temporary hard coding
        if str2num(Subjects{s}) == 3133
            best_angle(s) = 14-21;
        end
        if str2num(Subjects{s}) == 14839
            best_angle(s) = 1-21;
        end
        
    NMimage_rotated = imrotate(NMimage2D,best_angle(s));
    LCmask_rotated = imrotate(LCmask2D,best_angle(s));
    column_sum3=sum(LCmask_rotated);
    mask_indexAP=find(column_sum3>0);
    mask_front=max(mask_indexAP);
    column_sum4=sum(LCmask_rotated,2);
    mask_indexLR=find(column_sum4>0);
    ref_region_midline = round((min(mask_indexLR)+max(mask_indexLR))/2);
    ref_reg_mask=zeros(size(LCmask_rotated,1),size(LCmask_rotated,2));
    %ref_reg_mask(ref_region_midline-5:ref_region_midline+5,mask_front+6:mask_front+16)=1;
    ref_reg_mask(ref_region_midline-5:ref_region_midline+5,mask_front+16:mask_front+26)=1;
    ref_reg_unrotate = imrotate(ref_reg_mask,-best_angle(s));
    ref_reg_mask3D = LCmask;
    dim_change = (size(ref_reg_unrotate,1)-size(NMimage2D,1))/2;
    size(ref_reg_unrotate,1);
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % We commented out following line
    %ref_reg_mask3D(:,:,has_mask2)=ref_reg_unrotate(dim_change+1:size(ref_reg_unrotate,1)-dim_change,dim_change+1:size(ref_reg_unrotate,2)-dim_change);
    %v = spm_vol([root_folder '/LC subjects/LC' Subjects{s} 'nac.nii']);
    if LC_key(s,2)==1
    v.fname = [root_folder '/LC subjects/ref_LC' Subjects{s} 'nac.nii'];
    spm_write_vol(v,ref_reg_mask3D);
    elseif LC_key(s,2)==2
    v.fname = [root_folder '/LC subjects/ref_LC' Subjects{s} '.nii'];
    spm_write_vol(v,ref_reg_mask3D);
    elseif LC_key(s,2)==3
    v.fname = [root_folder '/LC subjects/cocaine/ref_LC' Subjects{s} '.nii'];
    spm_write_vol(v,ref_reg_mask3D);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    elseif LC_key(s,2)==4
    v.fname = [root_folder '/ref_LC' Subjects{s} '.nii'];
    spm_write_vol(v,ref_reg_mask3D);
    end
    ref_reg_data = NMimage_rotated(ref_reg_mask==1);
    [F,XI] = ksdensity(ref_reg_data);
    %figure;plot(XI,F)
for i= 1:length(F)
if F(i) ==max(F)
F_index(i) = 1;
else
F_index(i) = 0;
end
end
peak_smooth_DF(s)= XI(F_index==1);

    LC_CNR(s) = 100*((LCsignal(s) - peak_smooth_DF(s))./peak_smooth_DF(s))+100
end

