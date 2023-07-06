# Student Grades Prediction

This repository contains a Python code that demonstrates a simple data science approach to predicting students' final grades based on various attributes. The code utilizes popular data science libraries such as pandas, numpy, scikit-learn, and matplotlib.

## Dataset

The code uses the `student_mat.csv` dataset, which contains information about students' academic performance and other relevant attributes. The dataset includes the following columns:

- G1: First period grade (numeric: from 0 to 20)
- G2: Second period grade (numeric: from 0 to 20)
- G3: Final grade (numeric: from 0 to 20, output target)
- studytime: Weekly study time (numeric: 1 = <2 hours, 2 = 2 to 5 hours, 3 = 5 to 10 hours, 4 = >10 hours)
- absences: Number of school absences (numeric)
- failures: Number of past class failures (numeric)
- schoolsup: Extra educational support (categorical: "yes" or "no")
- famsup: Family educational support (categorical: "yes" or "no")

## Code Explanation

The code follows the following steps:

1. Importing the necessary libraries:
   - pandas is used for data manipulation and analysis.
   - numpy provides support for numerical operations.
   - scikit-learn offers machine learning algorithms and model evaluation tools.
   - matplotlib is utilized for data visualization.

2. Importing and preprocessing the dataset:
   - The dataset is loaded into a pandas DataFrame, specifying the separator as ";".
   - Only relevant attributes (columns) are selected for analysis.
   - Categorical attributes (schoolsup and famsup) are encoded into binary values for further processing.

3. Data cleaning and preparation:
   - Null entries are checked for and displayed.
   - Column names are cleaned and renamed for clarity and consistency.

4. Model training and evaluation:
   - The dataset is split into training and testing sets using scikit-learn's train_test_split function.
   - A linear regression model is instantiated and trained using the training data.
   - The accuracy of the model is calculated using the testing data.
   - The best-performing model i.e the model with the highest accuracy is saved using pickle serialization.

5. Model analysis and predictions:
   - The saved model is loaded from the pickle file.
   - Model coefficients (weights) and intercept are displayed.
   - The model is used to predict the final grades for the testing data.
   - Predicted grades, corresponding features, and actual labels are printed for analysis.

6. Data visualization:
   - Scatter plots are created to visualize the relationship between independent variables and the final grade.
   - Each plot represents the relationship between a specific attribute and the final grade.
   - The scatter plots are saved as a PDF file for further analysis.

## Instructions

To run the code and reproduce the results:

1. Ensure that you have Python installed on your machine.
2. Install the required libraries by running the following command:
   `pip install pandas numpy scikit-learn matplotlib`
3. Download the dataset file `student_mat.csv` and place it in the same directory as the code file.
4. Execute the code using a Python interpreter.
5. Review the output for model performance, predictions, and data visualization.

