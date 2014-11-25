from flask import Flask, render_template, request, session as websession
from model import PlaySession, dbsession
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from universals import data_dict, reversed_data_dict , columns_ordered_by_predictive_power,full_columns_ordered_by_predictive_power
import json

app = Flask(__name__)
app.secret_key = 'PredictionFTW'

forest = RandomForestClassifier(n_estimators = 100)

df = pd.read_csv('data cleaning and imputing/imputed.csv', header=0)

aggregated_df = pd.read_csv('data cleaning and imputing/aggregated.csv', header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
df = df.ix[:,1:]

@app.route("/")
def index():
	""" Home page """
	return render_template('index.html')

@app.route("/newgame")
def newgame():
	""" Clears old session and sets the items needed to render the base template (total foret's points, total player's points, and current question number) to 0 and the progress bar to 5% """
	websession.clear()
	websession['forets_points'] = 0
	websession['users_points'] = 0
	websession['current_q_numb'] = 0
	websession['progress_bar'] = 5
	return render_template('seed_questions.html', total_users_points = websession['users_points'], total_forets_points = websession['forets_points'], progress_bar = websession['progress_bar'], question_numb = websession['current_q_numb'])


@app.route("/question", methods = ["POST"])
def display_question():
	""" Main question page. Takes known data, runs it against the Random Forest model, makes a prediction. """

	global forest, df, aggregated_df

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

		# add playsession to database
		playsession.add_play_session()

		#add playsession ID to websession
		websession['session_id'] = playsession.session_id

		# set progress bar % to 10 (last page was 5%, goes up by 5% each time)
		websession['progress_bar'] = 10

	# continuing an existing game
	else:

		# get name of the last question answered from web session
		old_question_var_name = columns_ordered_by_predictive_power[websession['current_q_numb']]

		#get whatever they answered out of the form
		old_question_answer = request.form.get("question")
		
		# Get current playsession object out of database, using id stored in websession
		playsession = dbsession.query(PlaySession).get(websession['session_id'])

		# attach what they just submitted to playsession object
		setattr(playsession, old_question_var_name, old_question_answer)

		# up the count of the current question
		websession['current_q_numb'] += 1

		# up the progress bar by 5%. 
		websession['progress_bar'] += 5

		# if the last question submitted is the last one on in the list of questions, then commit the playsession and render the thank you template
		if old_question_var_name == columns_ordered_by_predictive_power[-1]:
			playsession.commit_play_session()
			return render_template('thank_you.html', total_forets_points = websession['forets_points'], total_users_points = websession['users_points'], progress_bar = websession['progress_bar'], question_numb = websession['current_q_numb'])

		#if it's not the last question, determine what the next question is and set up the test data
		else:
			new_question_var_name = columns_ordered_by_predictive_power[websession['current_q_numb']]

			# call the ordered parameter function on the playsession object to get all the questions answered to date. this will be the test data for the random forest model.
			test_data = playsession.ordered_parameter() 

	# determine what column number the current variable is in, to be used in setting up the training data
	column_of_var = full_columns_ordered_by_predictive_power.index(new_question_var_name) + 1  # + 1 because python slicing is not inclusive

	### Set up training data ###
	train_data = df.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable
	train_data_values = train_data.values #converting out of dataframe
	features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
	target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

	# Fit the training data to the target and create the decision trees
	forest = forest.fit(features_of_training_data, target_variable)

	# Predict the answer!
	predicted_new_question_answer = forest.predict(test_data)[0] #comes back as a one-item list.  sliced it down to a single number

	# Put predicted answer in websession
	websession['prediction'] = predicted_new_question_answer

	# add predicted new question answer to database, then commit
	predicted_new_question_var_name = "predicted_"+str(new_question_var_name)
	setattr(playsession, predicted_new_question_var_name, predicted_new_question_answer)
	playsession.commit_play_session()

	# title of new question to hand to html template
	new_question_title = data_dict[new_question_var_name]['title']

	# text of new question to hand to html template
	new_question_text = data_dict[new_question_var_name]['question']

	# Making two lists to hand to html template:
		# 1) List of answer option tuples (new_question_answer_list), for displaying the radio buttons
		# 2) List of data points for chart (data_for_chart)
	# Pulling from reversed data dict b/c 1) can use keys to create the order, and 2) already removed NaN's from reversed data dict
	new_question_answer_list = []
	data_for_chart = []
	for i in range(len(reversed_data_dict[new_question_var_name])):
		if new_question_var_name == 'income_distribution': #doesn't have a 0 answer so need to start at 1
			new_question_answer_list.append((i+1,reversed_data_dict[new_question_var_name][i+1]))
			data_for_chart.append(int(aggregated_df[new_question_var_name][i+1]*100 + .5)) #pulling data out of aggregated file, using current var name and number of answer option. Multiplying by 100 to make them percents, adding .5 to make int round correctly.
		else:
			new_question_answer_list.append((i,reversed_data_dict[new_question_var_name][i]))
			data_for_chart.append(int(aggregated_df[new_question_var_name][i]*100 + .5)) #pulling data out of aggregated file, using current var name and number of answer option. Multiplying by 100 to make them percents, adding .5 to make int round correctly.

	# Storing data for chart in websession to access later
	websession['data_for_chart'] = data_for_chart

	# Putting length of answer list in websession to calculate points per answer option later.
	websession['len_of_answer_list'] = len(new_question_answer_list)-1 # Minus one because if algorithm guesses exactly wrong, it should get 0 points

	# Storing predicted answer in websession to access later
	websession['predicted_new_question_answer'] = int(predicted_new_question_answer)


	return render_template('question.html', 

		# These three are used in question template
		new_question_text = new_question_text, 
		new_question_answer_list = new_question_answer_list,  
		new_question_title=new_question_title, 

		# These four are used in base template
		question_numb = websession['current_q_numb'], 
		total_users_points = websession["users_points"], 
		total_forets_points = websession["forets_points"], 
		progress_bar = websession['progress_bar'])



@app.route("/submitfirstanswer", methods = ["POST"])
def submit_first_answer():
	old_question_answer_numb = int(request.form.get("old_question_answer_numb"))
	# calculate the number of points foret gets for her algorithm guess
	points_per_answer = int(100/websession["len_of_answer_list"] + .5) #add .5 to make int round appropriately
	prediction=int(websession["prediction"])
	prediction_points = 100 - abs(old_question_answer_numb - prediction)*points_per_answer #points is a function of distance between predicted answer and submitted answer, plus number of answer choices. max for each q is 100, min is 0.
	if prediction_points < points_per_answer:
		prediction_points = 0 #necessary because of weirdness with decimal places. without this, points could be negative or other nonsensical numbers.


	#keep track of foret's total points tally
	websession["forets_points"] += prediction_points 


	to_send = {'prediction_points': prediction_points, 'predicted_new_question_answer': websession['predicted_new_question_answer'], 'total_forets_points': websession["forets_points"],}
	json_to_send = json.dumps(to_send)
	return json_to_send


@app.route("/submitsecondanswer", methods=["POST"])
def submit_second_answer():
	global aggregated_df

	#get submitted answers from form
	old_question_answer_numb = int(request.form.get("old_question_answer_numb"))
	guess = int(request.form.get("guess"))

	#determine what question we're on
	old_question_var_name = columns_ordered_by_predictive_power[websession['current_q_numb']]

	#pull the % of Americans who answered the same way as the respondent
	percent_who_answered_same_as_guess = int(aggregated_df[old_question_var_name][old_question_answer_numb] * 100 + .5) # add .5 to make sure the int rounds correctly



	# calculate the number of points the respondent gets for the accuracy of their guess
	guess_points = 100 - abs(percent_who_answered_same_as_guess - guess)*2 # points is the distance between your guess and the answer, such that a perfect guess is worth 100 points

	if guess_points < 0:
		guess_points = 0
	
	#keep track of user's total points tally
	websession["users_points"] += guess_points
	total_users_points = websession['users_points']

	#send all that data to custom.js
	to_send = {'guess': guess, 'percent_who_answered_same_as_guess': percent_who_answered_same_as_guess, 'guess_points': guess_points, 'total_users_points': total_users_points, 'data_for_chart': websession['data_for_chart'], 'predicted_new_question_answer':websession['predicted_new_question_answer'], 'old_question_var_name': old_question_var_name}
	json_to_send = json.dumps(to_send)

	return json_to_send

@app.route("/thank_you")
def thank_you():
	return render_template('thank_you.html', total_forets_points = websession['forets_points'], total_users_points = websession['users_points'], question_numb = websession['current_q_numb'])


@app.route("/about")
def about():
	return render_template('about.html', total_forets_points=websession["forets_points"],total_users_points=websession['users_points'], question_numb = websession['current_q_numb'])

if __name__ == "__main__":
	app.run(debug = True)