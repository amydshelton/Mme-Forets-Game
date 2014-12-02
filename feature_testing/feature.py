import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 100)

train_data = pd.read_csv('imputed.csv', header=0, index_col=0)

# train_data = df.ix[:,0:-1] #trimming it down to just the columns up to and 
# including the target variable
train_data_values = train_data.values #converting out of dataframe
features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus 
# last column, which is target variable
target_variable = train_data_values[0::,-1] # slices off the last column, 
# which is the target variable 

# Fit the training data to the target and create the decision trees
forest = forest.fit(features_of_training_data, target_variable)


## FIND OUT WHICH FEATURES MATTER
features = forest.feature_importances_
features.tofile('features.csv',sep=",")