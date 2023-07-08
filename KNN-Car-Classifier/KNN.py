import pandas as pd
import numpy as np
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model, preprocessing
import matplotlib.pyplot as plt

data = pd.read_csv("car.data")
# print(data.head())

predict = "class"

# Converting categorical data to numerical
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=0)

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
print(acc)

# Predicting the label
predicted = model.predict(X_test)

# Predictions vs Actual Values

names = ["unacc", "acc", "good", "vgood"]

for x in range(len(X_test)):
    print("Predictions: ", names[predicted[x]])
    print("Features: ", X_test[x])
    print("Actual Label: ", names[y_test[x]])
    n = model.kneighbors([X_test[x]], 9, True)
    print("N: ", n)
    print()

distances, indices = model.kneighbors([X_test[x]], 9, True)

# Extract the distances to the nearest neighbors
distances = distances[0]

# Plot the distances
plt.plot(range(1, 10), distances, marker='o')
plt.xlabel('Nearest Neighbor')
plt.ylabel('Distance')
plt.title('Distances to Nearest Neighbors')
plt.show()








