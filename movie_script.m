vidObj = VideoReader('color_test.mp4');
nFrames = vidObj.NumberOfFrames;
vidHeight = vidObj.Height;
vidWidth = vidObj.Width;
disp(nFrames);
%mov(1:nFrames) = struct('cdata', zeros(vidHeight, vidWidth, 3, 'uint8'));
edges = 1:128;
most_freq_index = 1:nFrames;
ccube = colorcube(128);
hex_vals = 1:nFrames;

t=cputime;
for i=1:nFrames
    im = read(vidObj, i);
    %quantize image
    
    qim = rgb2ind(im, ccube, 'nodither');
    %get the most frequent index
    [qim_w, qim_h] = size(qim);
    one_d = reshape(qim,1,(qim_w*qim_h));
    n_elements = histc(one_d, edges);
    [count, index] = max(n_elements);
    %store most frequent color
    most_freq_index(i) = index; 
end;
e = cputime-t

filename = 'colortest2.txt';
[fid, message] = fopen(filename, 'wt');

for row=1:nFrames
    index = most_freq_index(row);
    red_dec = floor(ccube(index,1)*255);
    green_dec = floor(ccube(index,2)*255);
    blue_dec = floor(ccube(index,3)*255);
    hex_s = strcat(dec2hex(red_dec,2), dec2hex(green_dec,2), dec2hex(blue_dec,2));
    fprintf(fid, '%s \n', hex_s);
end;

fclose(fid);