import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_diabetes
import streamlit as st
import base64
import plotly.graph_objects as go

#---------------------------------------------------------------#
# Page Layout

st.set_page_config(page_title='AutoForest',
                   layout='wide')

#---------------------------------------------------------------#
# Model Building

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="model_performance.csv">Download CSV File</a>'
    return href 

def build_model(df):
    X = df.iloc[:,:-1]
    Y = df.iloc[:,-1] # selects last column as target Y

    st.markdown('A model is being built to predict the following **Y** variable:')
    st.info(Y.name)

    st.markdown('**1.2. Data Splits**')
    st.write('Training Set')
    st.info(X.shape)
    st.write('Test Set')
    st.info(Y.shape)

    st.markdown('**1.3. Variable Details**')
    st.write('X Variable')
    st.info(list(X.columns))
    st.write('Y variable')
    st.info(Y.name)

    # Data splitting
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=split_size)

    rf = RandomForestRegressor(n_estimators=parameter_n_estimators,
                               random_state=parameter_random_state,
                               max_features=parameter_max_features,
                               criterion=parameter_criterion,
                               min_samples_leaf=parameter_min_samples_leaf,
                               bootstrap=parameter_bootstrap,
                               oob_score=parameter_oob_score,
                               n_jobs=parameter_n_jobs)
    
    grid = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
    grid.fit(X_train, y_train)


    st.subheader('Model Performance')

    Y_pred_test = grid.predict(X_test)
    st.write('Coefficient of determination ($R^2$):')
    st.info( r2_score(y_test, Y_pred_test) )

    st.write('Error (MSE or MAE):')
    st.info( mean_squared_error(y_test, Y_pred_test) )

    st.write("The best parameters are %s with a score of %0.2f"
      % (grid.best_params_, grid.best_score_))

    st.subheader('Model Parameters')
    st.write(grid.get_params())

     #-----Process grid data-----#
    grid_results = pd.concat([pd.DataFrame(grid.cv_results_["params"]),pd.DataFrame(grid.cv_results_["mean_test_score"], columns=["R2"])],axis=1)
    # Segment data into groups based on the 2 hyperparameters
    grid_contour = grid_results.groupby(['max_features','n_estimators']).mean()
    # Pivoting the data
    grid_reset = grid_contour.reset_index()
    grid_reset.columns = ['max_features', 'n_estimators', 'R2']
    grid_pivot = grid_reset.pivot('max_features', 'n_estimators')
    x = grid_pivot.columns.levels[1].values
    y = grid_pivot.index.values
    z = grid_pivot.values

    #-----Plot-----#
    layout = go.Layout(
            xaxis=go.layout.XAxis(
              title=go.layout.xaxis.Title(
              text='n_estimators')
             ),
             yaxis=go.layout.YAxis(
              title=go.layout.yaxis.Title(
              text='max_features')
            ) )
    fig = go.Figure(data= [go.Surface(z=z, y=y, x=x)], layout=layout )
    fig.update_layout(title='Hyperparameter tuning',
                      scene = dict(
                        xaxis_title='n_estimators',
                        yaxis_title='max_features',
                        zaxis_title='R2'),
                      autosize=False,
                      width=800, height=800,
                      margin=dict(l=65, r=50, b=65, t=90))
    st.plotly_chart(fig)

     #-----Save grid data-----#
    x = pd.DataFrame(x)
    y = pd.DataFrame(y)
    z = pd.DataFrame(z)
    df = pd.concat([x,y,z], axis=1)
    st.markdown(filedownload(grid_results), unsafe_allow_html=True)


#---------------------------------------------------------------#
st.write("""
# AutoForest: Automated ML with Random Forest
         
An implementation of the **Random Forest** algorithm. Just upload data, customize random forest parameters, and let the magic unfold. No coding needed, just results.

Try adjusting the hyperparameters in the sidebar!

""")

#---------------------------------------------------------------#

# Sidebar - collect user input
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file",type=["csv"])

    
# Sidebar - specify parameter settings
with st.sidebar.header('2. Set Parameters'):
    split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80,5)

with st.sidebar.subheader('2.1. Learning Parameters'):
    parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 0, 500, (10,50), 50)
    parameter_n_estimators_step = st.sidebar.number_input('Step size for n_estimators', 10)
    st.sidebar.write('---')
    parameter_max_features = st.sidebar.slider('Max features (max_features)', 1, 50, (1,3), 1)
    st.sidebar.number_input('Step size for max_features', 1)
    st.sidebar.write('---')
    parameter_min_samples_split = st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)', 1, 10, 2, 1)
    parameter_min_samples_leaf = st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)', 1, 10, 2, 1)

with st.sidebar.subheader('2.2. General Parameters'):
    parameter_random_state = st.sidebar.slider('Seed number (random_state)', 0, 1000, 42, 1)
    parameter_criterion = st.sidebar.select_slider('Performance measure (criterion)', options=['squared_error', 'absolute_error'])
    parameter_bootstrap = st.sidebar.select_slider('Bootstrap samples when building trees (bootstrap)', options=[True, False])
    parameter_oob_score = st.sidebar.select_slider('Whether to use out-of-bag samples to estimate the R^2 on unseen data (oob_score)', options=[False, True])
    parameter_n_jobs = st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)', options=[1, -1])

n_estimators_range = np.arange(parameter_n_estimators[0], parameter_n_estimators[1]+parameter_n_estimators_step, parameter_n_estimators_step)
max_features_range = np.arange(parameter_max_features[0], parameter_max_features[1]+1, 1)
param_grid = dict(max_features=max_features_range, n_estimators=n_estimators_range)

#---------------------------------------------------------------#
# Main Panel

# display dataset
st.subheader('1. Dataset')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown('**1.1. Glimpse of dataset**')
    st.write(df)
    build_model(df)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Diabetes dataset
        diabetes = load_diabetes()
        X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        Y = pd.Series(diabetes.target, name='response')
        df = pd.concat( [X,Y], axis=1 )

        st.markdown('The Diabetes dataset is used as the example.')
        st.write(df.head(5))

        build_model(df)




