from flask import Flask, render_template, redirect, request, session as websession
from model import PlaySession, dbsession
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from universals import data_dict, reversed_data_dict , column_order


app = Flask(__name__)
app.secret_key = 'PredictionFTW'

forest = RandomForestClassifier(n_estimators = 100)

df = pd.read_csv('data cleaning and imputing/imputed.csv', header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
df = df.ix[:,1:]


@app.route("/")
def index():
    return render_template('seed_questions.html')

@app.route("/religious", methods = ["POST"])
def first_question():
	global data_dict, reversed_data_dict, forest, df

	age = int(request.form.get("age"))
	sex = data_dict['sex']['answers'][str(request.form.get("sex"))]
	race = data_dict['race']['answers'][str(request.form.get("race"))]
	region = data_dict['region']['answers'][str(request.form.get("region"))]
	highest_grade = int(request.form.get("highest-grade"))
	employment_status = data_dict['employment_status']['answers'][str(request.form.get("employment-status"))]
	marital_status = data_dict['marital_status']['answers'][str(request.form.get("marital-status"))]

	new_question_var_name = column_order[0]	

	column_of_var = column_order.index(new_question_var_name) + 8 #because there are 7 demographic questions before the predictable questions begin, and we need to slice up to current column plus one b/c range of slice is not inclusive

	train_data = df.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable

	train_data_values = train_data.values #converting out of dataframe

	features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
	target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

	# # Fit the training data to the target and create the decision trees
	forest = forest.fit(features_of_training_data, target_variable)

	test_data = [age, sex, race, region, highest_grade, employment_status, marital_status]

	# # Take the same decision trees and run it on the test data
	predicted_new_question_answer = forest.predict(test_data)[0] #comes back as a one-item list.  sliced it down to a single number

	playsession = PlaySession(age = age, sex = sex, race = race, region = region, highest_grade = highest_grade, employment_status = employment_status, marital_status = marital_status, predicted_religious = predicted_new_question_answer)

	playsession.add_play_session()

	websession['session_id'] = playsession.session_id
	websession['current_q_numb'] = 0


	
	predicted_new_question_translated = reversed_data_dict[new_question_var_name][int(predicted_new_question_answer)]

	#text of new question to hand to html template
	new_question_text = data_dict[new_question_var_name]['question']

	# making a list of answer options to hand to the html template. Pulling form reversed data dict b/c 1) can use keys to create the order, and 2) already removed NaN's from reversed data dict
	new_question_answer_list = []
	for i in range(len(reversed_data_dict[new_question_var_name])):
		new_question_answer_list.append(reversed_data_dict[new_question_var_name][i])

	return render_template('question.html',  predicted_new_question_translated = predicted_new_question_translated, new_question_var_name = new_question_var_name, new_question_answer_list = new_question_answer_list, new_question_text =new_question_text)


@app.route("/nextquestion", methods = ["POST"])
def next_question():
	global data_dict, reversed_data_dict, forest, df, column_order

	old_question_var_name = column_order[websession['current_q_numb']]
	old_question_answer = data_dict[old_question_var_name]['answers'][str(request.form.get(old_question_var_name))]
	# Get current playsession object out of database, using id stored in websession
	playsession = dbsession.query(PlaySession).get(websession['session_id'])

	setattr(playsession, old_question_var_name, old_question_answer)

	if column_order.index(old_question_var_name) == 25:

		return render_template('thank_you.html')

	else:
		new_question_var_name = column_order[websession['current_q_numb']+1]
		
		
		column_of_var = column_order.index(new_question_var_name) + 8 #because there are 7 demographic questions before the predictable questions begin, and we need to slice up to current column plus one b/c range of slice is not inclusive

		### Set up training data ###
		train_data = df.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable
		train_data_values = train_data.values #converting out of dataframe
		features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
		target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

		# Fit the training data to the target and create the decision trees
		forest = forest.fit(features_of_training_data, target_variable)

		test_data = playsession.ordered_parameter() 

		
		predicted_new_question_answer = forest.predict(test_data)[0] #comes back as a one-item list.  sliced it down to a single number

		# add stated old question answer and predicted new question answer to database, then commit
		predicted_new_question_var_name = "predicted_"+str(new_question_var_name)
		setattr(playsession, predicted_new_question_var_name, predicted_new_question_answer)
		playsession.commit_play_session()

		predicted_new_question_translated = reversed_data_dict[new_question_var_name][int(predicted_new_question_answer)]

		websession['current_q_numb'] += 1

		#text of new question to hand to html template
		new_question_text = data_dict[new_question_var_name]['question']

		# making a list of answer options to hand to the html template. Pulling form reversed data dict b/c 1) can use keys to create the order, and 2) already removed NaN's from reversed data dict
		new_question_answer_list = []
		for i in range(len(reversed_data_dict[new_question_var_name])):
			questions_without_0_answer = ['income_distribution','govt_help_poor','govt_help_sick','govt_more_less','govt_help_blacks']
			if new_question_var_name in questions_without_0_answer:
				new_question_answer_list.append(reversed_data_dict[new_question_var_name][i+1])
			else:
				new_question_answer_list.append(reversed_data_dict[new_question_var_name][i])

		return render_template('question.html', predicted_new_question_translated = predicted_new_question_translated, new_question_var_name = new_question_var_name, new_question_text = new_question_text, new_question_answer_list = new_question_answer_list)



if __name__ == "__main__":
    app.run(debug = True)