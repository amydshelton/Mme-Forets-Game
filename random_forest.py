import pandas as pd 
# import numpy as np

df = pd.read_csv('train.csv', header=0)

train_data = df.values

df2 = pd.read_csv('test.csv', header=0)

test_data = df2.values

# print test_data

# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 

# # Create the random forest object which will include all the parameters
# # for the fit
forest = RandomForestClassifier(n_estimators = 100)

# # Fit the training data to the Survived labels and create the decision trees
forest = forest.fit(train_data[0::,0:-1:],train_data[0::,-1])

# # Take the same decision trees and run it on the test data
output = forest.predict(test_data[0::,0:-1:])

#make output into list
output = output.tolist()

# print output

#appending output to test data to see how I did
for i in range(len(test_data)):
	list_from_td = test_data[i].tolist()
	list_from_td.append(output[i])
	print list_from_td

#got a 60% accuracy on working fulltime