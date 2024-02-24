 %Load the dataset information from the MAT file
load('./Trainset.mat');

%%
% Create an image datastore from the loaded information
imds = imageDatastore(datasetPath, ...
    'IncludeSubfolders', true, ...
    'LabelSource', 'foldernames');

% Split the dataset into training and validation sets
numTrainingFiles = 750;
[imdsTrain, imdsTest] = splitEachLabel(imds, numTrainingFiles, 'randomize');
%%
% Defining CNN architecture
layers = [
    imageInputLayer([92 92 3])
    convolution2dLayer(3, 16, 'Padding', 'same')
    reluLayer
    maxPooling2dLayer(2, 'Stride', 2)
    convolution2dLayer(3, 64, 'Padding', 'same')
    reluLayer
    maxPooling2dLayer(2, 'Stride', 2)
    fullyConnectedLayer(2)
    softmaxLayer
    classificationLayer 
];
%%
% Set training options
options = trainingOptions('sgdm', ...
    'MiniBatchSize', 32, ...
    'InitialLearnRate', 1e-6, ...
    'MaxEpochs', 10);
%%
% Train the CNN
net = trainNetwork(imdsTrain, layers, options);
%%
% Make predictions on a test image
img = imread('dataset/test.jpg');
prediction = classify(net, img);
%%
% Display the result
disp(['Prediction: ', char(prediction)]);
