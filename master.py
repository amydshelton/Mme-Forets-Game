from flask import Flask, render_template, request, session as websession
from model import PlaySession, dbsession
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from universals import data_dict, reversed_data_dict , columns_ordered_by_predictive_power,full_columns_ordered_by_predictive_power


app = Flask(__name__)
app.secret_key = 'PredictionFTW'

forest = RandomForestClassifier(n_estimators = 100)

df = pd.read_csv('data cleaning and imputing/imputed.csv', header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
df = df.ix[:,1:]


@app.route("/")
def index():
	websession.clear()
	return render_template('seed_questions.html')


@app.route("/nextquestion", methods = ["POST"])
def display_question():
	global forest, df

	## if starting a new game:
	if 'session_id' not in websession:

		#get out of the form the items put in
		age = int(request.form.get("age"))
		highest_grade = int(request.form.get("highest-grade"))


		#this will be the data the model uses to predict the answer to the next question
		test_data = [age, highest_grade]

		# variable name is the first one in the order of questions
		new_question_var_name = columns_ordered_by_predictive_power[0]	

		# instantiate playsession
		playsession = PlaySession(age = age, highest_grade = highest_grade)

		# add
		playsession.add_play_session()

		#add playsession ID to websession
		websession['session_id'] = playsession.session_id

		# keep track of what question number we're on in the websession
		websession['current_q_numb'] = 0

		# set foret's points equal to 0
		websession['forets_points'] = 0
		

	#continuing an existing game
	else:

		# get name of the last question answered from web session
		old_question_var_name = columns_ordered_by_predictive_power[websession['current_q_numb']]

		#get whatever they answered out of the form
		old_question_answer = request.form.get("question")
		

		# Get current playsession object out of database, using id stored in websession
		playsession = dbsession.query(PlaySession).get(websession['session_id'])

		# attach what they just submitted to playsession object
		setattr(playsession, old_question_var_name, old_question_answer)

		# up the cound of the current question
		websession['current_q_numb'] += 1

		#if the last question submitted is the last one on in the list of questions (aka #18 ), then commit the playsession and render the thank you template
		if columns_ordered_by_predictive_power.index(old_question_var_name) == 17:
			playsession.commit_play_session()
			return render_template('thank_you.html')

		#if it's not the last question, determine what the next question is and set up the test data
		else:
			new_question_var_name = columns_ordered_by_predictive_power[websession['current_q_numb']]
			test_data = playsession.ordered_parameter() 

	column_of_var = full_columns_ordered_by_predictive_power.index(new_question_var_name) + 1  # + 1 because python slicing is not inclusive

	### Set up training data ###
	train_data = df.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable
	train_data_values = train_data.values #converting out of dataframe
	features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
	target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

	# Fit the training data to the target and create the decision trees
	forest = forest.fit(features_of_training_data, target_variable)

	
	predicted_new_question_answer = forest.predict(test_data)[0] #comes back as a one-item list.  sliced it down to a single number

	websession['prediction'] = predicted_new_question_answer

	# add stated old question answer and predicted new question answer to database, then commit
	predicted_new_question_var_name = "predicted_"+str(new_question_var_name)
	setattr(playsession, predicted_new_question_var_name, predicted_new_question_answer)
	playsession.commit_play_session()

	predicted_new_question_translated = reversed_data_dict[new_question_var_name][int(predicted_new_question_answer)]

	#title of new question to hand to html template
	new_question_title = data_dict[new_question_var_name]['title']

	#text of new question to hand to html template
	new_question_text = data_dict[new_question_var_name]['question']

	# making a list of answer options to hand to the html template. Pulling from reversed data dict b/c 1) can use keys to create the order, and 2) already removed NaN's from reversed data dict
	new_question_answer_list = []
	for i in range(len(reversed_data_dict[new_question_var_name])):
		questions_without_0_answer = ['income_distribution','govt_help_poor','govt_help_sick','govt_more_less','govt_help_blacks']
		if new_question_var_name in questions_without_0_answer:
			new_question_answer_list.append((i+1,reversed_data_dict[new_question_var_name][i+1]))
		else:
			new_question_answer_list.append((i,reversed_data_dict[new_question_var_name][i]))

	websession['len_of_answer_list'] = len(new_question_answer_list)-1 # Will use this to calculate points. Minus one because if algorithm guesses exactly wrong, it should get 0 points

	return render_template('question.html', predicted_new_question_translated = predicted_new_question_translated, new_question_var_name = new_question_var_name, new_question_text = new_question_text, new_question_answer_list = new_question_answer_list, new_question_title=new_question_title, question_numb = websession['current_q_numb']+1)


@app.route("/submitanswer", methods=["POST"])
def submit_answer():
	old_question_answer_numb = int(request.form.get("old_question_answer_numb"))
	points_per_answer = 100/int(websession["len_of_answer_list"])
	prediction=int(websession["prediction"])
	points = 100 - abs(old_question_answer_numb - prediction)*points_per_answer #points is a function of distance between predicted answer and submitted answer, plus number of answer choices. max for each q is 100, min is 0.
	if points == 1:
		points = 0
	websession["forets_points"] += points  # this needs to be handed to template too
	print websession["forets_points"]
	return str(points)

if __name__ == "__main__":
	app.run(debug = True)