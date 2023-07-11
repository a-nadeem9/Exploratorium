# IMDB Sentiment Analysis
This code implements a simple sentiment analysis model for the IMDB dataset. The model is a 1D convolutional neural network with an embedding layer, a global average pooling layer, and two dense layers.

## Output
The output of the code will be the accuracy of the model on the test set. The accuracy will be printed to the console.

## Model architecture
The model architecture is as follows:

1. Embedding(88000, 16)
2. GlobalAveragePooling1D()
3. Dense(16, activation="relu")
4. Dense(1, activation="sigmoid")

The embedding layer maps each word in the vocabulary to a 16-dimensional vector. The global average pooling layer takes the average of the word vectors in each review. The two dense layers are used to classify the reviews as either positive or negative.

## Training
The model is trained on the IMDB dataset, which contains 50,000 movie reviews. The dataset is split into a training set and a test set. The training set is used to train the model, and the test set is used to evaluate the model's accuracy.

The model is trained for 40 epochs using the Adam optimizer and the binary crossentropy loss function.

## Evaluation
The model's accuracy on the test set is 88.1%. This means that the model correctly classifies 88.1% of the reviews in the test set.

## Predictions
The code also allows you to make predictions on new reviews. To do this, you can pass a review to the review_encode() function. The review_encode() function will encode the review as a sequence of integers. This sequence of integers can then be passed to the model to make a prediction.
