# AutoForest: Automated ML with Random Forest

AutoForest is a web application that allows you to effortlessly build a machine learning regression model by uploading a CSV file. The application leverages the power of Random Forest, a popular ensemble learning algorithm, and provides a user-friendly interface to customize the model's parameters without writing any code.

## How it Works

1. **Upload your CSV data**: To get started, upload your CSV file containing the data you want to build the regression model on. The application will process the data and display a preview of the dataset.

2. **Set Parameters**: Next, specify the parameter settings for the Random Forest algorithm. You have the flexibility to adjust various hyperparameters, such as the number of estimators, maximum features, minimum samples required to split an internal node, and minimum samples required to be at a leaf node.

3. **Model Building**: Once you've uploaded the data and set the parameters, AutoForest will split the dataset into training and test sets based on the specified ratio. The Random Forest regression model will be trained on the training set using the provided parameters.

4. **Model Performance**: After building the model, the application will evaluate its performance on the test set. It will display two important metrics:
   - Coefficient of determination ($R^2$): A measure of how well the model fits the data.
   - Error (MSE or MAE): An indication of the model's predictive accuracy.

5. **Hyperparameter Tuning Visualization**: AutoForest goes one step further by visualizing the hyperparameter tuning process. The application generates a 3D surface plot that shows how different combinations of `n_estimators` and `max_features` affect the model's $R^2$ score. This visualization helps you gain insights into how changing these hyperparameters impacts the model's performance.

6. **Download Model Performance Data**: You can download a CSV file containing detailed information about the model's performance across different hyperparameter settings. This data can be valuable for further analysis and comparison.

## Example Dataset

If you don't have a CSV file ready, you can use the example dataset provided by AutoForest. The example dataset used in this application is the Diabetes dataset, which comes bundled with the popular Scikit-learn library.

## How to Use

1. Upload your CSV file by clicking on the "Upload your input CSV file" button in the sidebar.

2. Set the Random Forest parameters by adjusting the sliders and select sliders in the sidebar.

3. Press the "Press to use Example Dataset" button if you want to use the provided Diabetes dataset.

4. Observe the model performance metrics and hyperparameter tuning visualization in the main panel.

5. Download the detailed model performance data as a CSV file by clicking on the "Download CSV File" link.

