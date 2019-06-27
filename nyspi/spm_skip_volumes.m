function images = spm_skip_volumes(F, K, varargin)
% spm_skip_volumes  - skip K volumes in NIFTI file F
% FORMAT spm_skip_volumes(F, K)
% F    - filename of NIFTI file
% K    - number of volumes to skip from beginning (in addition to already skipped!)

% check inputs
if nargin < 2 || ~ischar(F) || isempty(F) || ~isa(K, 'double') || numel(K) ~= 1 || K < 1 || isinf(K) || isnan(K)
    error('insufficient or bad arguments.');
end


if isempty(varargin)
    prf = 't';
else
    prf = varargin{1};
end

% ensure K is integer
K = floor(K);

% ensure file exists
if exist(F, 'file') ~= 2
    error('NIFTI file in F doesn''t exist.');
end

% open file
fid = fopen(F, 'r+', 'ieee-le');
if fid < 1
    error('error opening NIFTI file.');
end

% get filesize
fseek(fid, 0, 1);
filesize = ftell(fid);
if filesize < 400
    fclose(fid);
    error('NIFTI file in F too short.');
end
fseek(fid, 0, -1);

% confirm it's a regular NIFTI file
byte_check = fread(fid, [1, 4], 'uint8=>double');
if ~isequal(byte_check, [92, 1, 0, 0])

    % close file
    fclose(fid);

    % could be big-endian, if so, re-open
    if isequal(byte_check, [0, 0, 1, 92])
        fid = fopen(F, 'r+', 'ieee-be');

    % or not...
    else
        error('file in F not a NIFTI file.');
    end
end

% seek forward to position 40, read dimensions
fseek(fid, 40, -1);
D = fread(fid, [1, 8], 'uint16=>double');

% check D(1)
if D(1) ~= 4
    fclose(fid);
    error('NIFTI file in F not a 4D volume series.');
end

% check D(5) (4-th dim) to be > K
if D(5) <= K
    fclose(fid);
    error('NIFTI file in F has too few volumes to skip additional K volumes.');
end

% seek forward to position 72, read bits per pixel header info
fseek(fid, 72, -1);
bitsperpixel = fread(fid, [1, 1], 'uint16=>double');
bytesperpixel = ceil(bitsperpixel / 8);

% seek forward to position 108, read current voxel offset
fseek(fid, 108, -1);
voxoffset = fread(fid, [1, 1], 'single=>double');

% check filesize
compsize = voxoffset + bytesperpixel * prod(D(2:5));
if compsize > filesize
    fclose(fid);
    error('NIFTI file in F too short.');
end

% compute new offset
newoffset = voxoffset + bytesperpixel * prod(D(2:4)) * K;

% ensure that new offset can be represented as a single
if newoffset ~= double(single(newoffset))
    fclose(fid);
    error('NIFTI header in F cannot be patched due to precision error in offset.');
end

% re-seek to position 48, write new number of volumes
fseek(fid, 48, -1);
fwrite(fid, uint16(D(5) - K), 'uint16');

% re-seek to position 108, write new offset
fseek(fid, 108, -1);
fwrite(fid, single(newoffset), 'single');

% close file
fclose(fid);

path = pwd
file_path = fullfile(path, 'y.nii')

[pp,ff,xx] = fileparts(F);
images = [pp filesep prf ff xx];
save(file_path, images);

end
