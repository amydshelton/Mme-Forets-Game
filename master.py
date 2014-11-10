from flask import Flask, render_template, redirect, request, session as websession
from model import PlaySession
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from data_dict import data_dict, reversed_data_dict 


app = Flask(__name__)
app.secret_key = 'PredictionFTW'

forest = RandomForestClassifier(n_estimators = 100)

df = pd.read_csv('data cleaning and imputing/imputed.csv', header=0)

df = df.ix[:,1:]


@app.route("/")
def index():
    return render_template('seed_questions.html')

@app.route("/religious", methods = ["POST"])
def first_question():
	global data_dict, reversed_data_dict, forest, df

	age = int(request.form.get("age"))
	sex = data_dict['sex'][str(request.form.get("sex"))]
	race = data_dict['race'][str(request.form.get("race"))]
	region = data_dict['region'][str(request.form.get("region"))]
	highest_grade = int(request.form.get("highest-grade"))
	employment_status = data_dict['employment_status'][str(request.form.get("employment-status"))]
	marital_status = data_dict['marital_status'][str(request.form.get("marital-status"))]


	# run random forest, given current info, to preduct employment status
	# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
	

	column_of_var = 8

	train_data = df.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable

	train_data_values = train_data.values #converting out of dataframe

	features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
	target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

	# # Fit the training data to the target and create the decision trees
	forest = forest.fit(features_of_training_data, target_variable)

	test_data = [age, sex, race, region, highest_grade, employment_status, marital_status]

	# # Take the same decision trees and run it on the test data
	predicted_religiosity = forest.predict(test_data)[0] #comes back as a one-item list.  sliced it down to a single number


	predicted_religiosity_translated = reversed_data_dict['religious'][int(predicted_religiosity)]

	playsession = PlaySession(age = age, sex = sex, race = race, region = region, highest_grade = highest_grade, employment_status = employment_status, marital_status = marital_status, predicted_religiosity = predicted_religiosity)

	playsession.add_play_session()


	return render_template('first_question.html', playsession = playsession, predicted_religiosity_translated = predicted_religiosity_translated)

if __name__ == "__main__":
    app.run(debug = True)