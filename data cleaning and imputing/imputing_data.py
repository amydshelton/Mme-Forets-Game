import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
import sys
import numpy as np

sys.path.append("/Users/greglaughlin/Desktop/Hackbright/HB_Project")

from universals import column_order

forest = RandomForestClassifier(n_estimators = 100)

df = pd.read_csv("cleaned.csv", header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
df = df.ix[:,1:]


for i in range(len(column_order)):

	variable = column_order[i]

	column_of_var = i + 42 #because there are 8 columns before these columns with basic demographic info (age, sex, etc.) where I imputed based on the median/most common answer

	train_data = df.loc[pd.isnull(df[variable])==False] #training data is the data where we have an answer for the target variable

	train_data = train_data.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable

	train_data_values = train_data.values #converting out of dataframe

	test_data = df.loc[pd.isnull(df[variable])] #test data is the data where we don't have an answer for the target variable

	test_data = test_data.ix[:,0:column_of_var-1] #trimming down to just the columns up to the target variable

	test_data_values = test_data.values #converting out of dataframe

	features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
	target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

	# develop prediction model
	forest = forest.fit(features_of_training_data, target_variable)

	# take the same model and run it on the test data
	output = forest.predict(test_data_values)

	# now that we have a prediction, we need to update our dataset with that prediction

	# first, pull out the list of ID numbers for the people we predicted
	ids_from_test_data = test_data.index

	# then update the dataframe with their personalized prediction
	for i in range(len(ids_from_test_data)):
		df[variable][ids_from_test_data[i]] = output[i] #sets previously empty cell equal to prediction





# #put income_bucket in the right spot in the df, where income was
# full_column_order = ['age', 'sex', 'race', 'region', 'highest_grade', 'employment_status', 'marital_status',] + column_order

# new_df = df[full_column_order]




# # save file

# new_df.to_csv('imputed.csv')

df.to_csv('imputed.csv')


