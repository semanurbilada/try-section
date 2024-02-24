% % Specify the path to your image dataset
% datasetPath = './subdatasets';
% 
% % Create imageDatastore for your dataset
% imds = imageDatastore(datasetPath, 'IncludeSubfolders', true, 'LabelSource', 'foldernames');
% 
% % Create a structure to store the necessary information
% datasetInfo = struct('datasetPath', datasetPath, 'imds', imds);
% 
% % Save the structure to a MAT file
% save('brainTumor_dataset.mat', 'datasetInfo');

pic1 = imread('file_path/dataset/*.jpg');
save('BothPics.mat', 'pic1');