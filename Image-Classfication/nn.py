import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# import dataset from keras
data = keras.datasets.fashion_mnist

# Splitting datat into training and test sets.
(train_images, train_labels), (test_images, test_labels) = data.load_data()

# Labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

# # Plotting to access the data
# plt.imshow(train_images[7], cmap=plt.cm.binary)
# plt.show()

# Shrinking the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Defining architecture/layers for our model
model = keras.Sequential([

    # We need to flatten the data, so it is passable to all neurons as opposed to sending a whole list to each neuron.
    keras.layers.Flatten(input_shape=(28, 28)),

    # "Dense" layer essentially means fully connected layer.
    # Activation function "relu" works well and fast for a variety of applications.
    keras.layers.Dense(128, activation="relu"),

    # Another dense layer, with the activation of 'softmax'. It will pick values for reach of the neurons in such a way that all values add up to one.
    keras.layers.Dense(10, activation="softmax")
])

# Setting up parameters for the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Fitting the model
model.fit(train_images, train_labels, epochs=5)  # epochs: how many times the model will see the training information.


test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Tested Accuracy: ", test_acc)

# Making predictions
prediction = model.predict(test_images)

# Comparing Predictions vs. Actual labels.
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[i])])
    plt.show()


