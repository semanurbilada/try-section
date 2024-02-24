%% TESTING: Train R-CNN Stop Sign Detector
% 
%%
% Load training data and network layers.
load('rcnnStopSigns.mat', 'stopSigns', 'layers')
%%
options = trainingOptions('sgdm', ...
  'MiniBatchSize', 32, ...
  'InitialLearnRate', 1e-6, ...
  'MaxEpochs', 10);

%%
% Train the R-CNN detector. Training can take a few minutes to complete.
rcnn = trainRCNNObjectDetector(stopSigns, layers, options, 'NegativeOverlapRange', [0 0.3]);

%%
% Test the R-CNN detector on a test image.
img = imread('stopSignTest.jpg'); 

[bbox, score, label] = detect(rcnn, img, MiniBatchSize=32);
%%
% Display strongest detection result.
[score, idx] = max(score);

bbox = bbox(idx, :);
annotation = sprintf('%s: (Confidence = %f)', label(idx), score);

detectedImg = insertObjectAnnotation(img, 'rectangle', bbox, annotation);

figure
imshow(detectedImg)
