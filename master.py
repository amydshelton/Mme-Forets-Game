from flask import Flask, render_template, redirect, request, session as websession
from model import PlaySession, dbsession
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier 


app = Flask(__name__)
app.secret_key = 'PredictionFTW'

@app.route("/")
def index():
    return render_template('seed_questions.html')

@app.route("/1", methods = ["POST"])
def first_question():
	seed_questions = {'Male':1, 'Female':0, 'Asian':1, 'Black':2, 'Hispanic':3, 'Other':4, 'White':5, 'ENC':1, 'ESC':2, 'MA':3, 'Mtn':4, 'NE':5, 'Pa':6, 'SA':7, 'WNC':8, 'WSC':9}

	age = int(request.form.get("age"))
	sex = seed_questions[str(request.form.get("sex"))]
	race = seed_questions[str(request.form.get("race"))]
	region = seed_questions[str(request.form.get("region"))]
	highest_grade = int(request.form.get("highest-grade"))


	# run random forest, given current info, to preduct employment status
	df = pd.read_csv('train.csv', header=0)

	train_data = df.values

	forest = RandomForestClassifier(n_estimators = 100)

	# # Fit the training data to the employment status labels and create the decision trees
	forest = forest.fit(train_data[0::,0:-1:],train_data[0::,-1])

	test_data = [age, sex, race, region, highest_grade]

	# # Take the same decision trees and run it on the test data
	predicted_employment_status = forest.predict(test_data)[0]

	employment_dict = {'1': "Keeping House", '2': "Other", '3': "Retired", '4': "School", '5':"Temp Not Working", '6':"Unemployed", '7':"Working Fulltime", '8': "Working Parttime", '9':"Unknown"}
	predicted_employment_status_translated = employment_dict[str(predicted_employment_status)]

	playsession = PlaySession(age = age, sex = sex, race = race, region = region, highest_grade = highest_grade, predicted_employment_status = predicted_employment_status)
	dbsession.add(playsession)
	dbsession.commit()

	return render_template('first_question.html', playsession = playsession, predicted_employment_status_translated = predicted_employment_status_translated)

if __name__ == "__main__":
    app.run(debug = True)