import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

# Importing data, and since our data is seperated by ';' we need to do sep=";"
data = pd.read_csv('student_mat.csv', sep=";")
# print(data.head())


# Keeping the "relevant" attributes(columns)
data = data[['G1', 'G2', 'G3', 'studytime', "absences", "failures", "schoolsup", "famsup"]]

# Checking the relationship between the categorical data
print(data["schoolsup"].value_counts())
print(data["famsup"].value_counts())

# using binary encoding
data["schoolsup"] = data["schoolsup"].map({"yes": 1, "no": 0})
data["famsup"] = data["famsup"].map({"yes": 1, "no": 0})
data.info()

# Checking for null entries
print(data.isna().sum())

# Cleaning column names
data = data.rename(columns={"G3": "final_grade", "studytime": "study_time", "schoolsup": "school_sup", "famsup": "fam_sup"})

# We are trying to predict the final grade label i.e. G3
predict = "final_grade"

# Features/Attributes
X = np.array(data.drop([predict], axis=1))
# Label
y = np.array(data[predict])

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

best = 0
for _ in range(30):
    # Splitting testing & training dataset
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    # Creating instance of the LinearRegression() class
    linear = linear_model.LinearRegression()

    # fitting the data to find the best fit line
    linear.fit(X_train, y_train)

    # Calculating accuracy of the model
    acc = linear.score(X_test, y_test)
    print(acc)

    if acc > best:
        best = acc
        # Don't need to save the model but I'm still going to do it
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)


# Reading in the Pickle file
pickle_in = open("studentgrades.pickle", "rb")

# Loading the pickle into our linear model
linear = pickle.load(pickle_in)

print("Coefficient: ", linear.coef_)
print("Intercept:", linear.intercept_)

# Predicting the label using testing data
predictions = linear.predict(X_test)

for x in range(len(predictions)):
    print("Predictions: ",round(predictions[x]))
    print("Features: ",X_test[x])
    print("Actual Label: ",y_test[x])
    print()

# Creating a scatter plot for each independent variable
style.use("ggplot")
def create_scatter_plot(x, y, title, ax):
    ax.scatter(x, y, color='blue')
    ax.set_title(title)

# Creating a scatter plot for each independent variable to check linearity
fig, axes = plt.subplots(2, 4, figsize=(16, 6))

variables = ["G1", "G2", "study_time", "absences", "failures", "school_sup", "fam_sup"]
titles = ["G1 and Final Grade", "G2 and Final Grade", "Study Time and Final Grade", "Absences and Final Grade",
          "Failures and Final Grade", "School Support and Final Grade", "Family Support and Final Grade"]

for i, var in enumerate(variables):
    row = i // 4
    col = i % 4
    create_scatter_plot(data[var], data["final_grade"], titles[i], axes[row, col])

fig.delaxes(axes[1, 3])

plt.subplots_adjust(hspace=0.5)
plt.tight_layout()
plt.show()
fig.savefig("scatter_plots.pdf")