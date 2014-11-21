from flask import Flask, render_template, request, session as websession
from model import PlaySession, dbsession
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from universals import data_dict, reversed_data_dict , columns_ordered_by_predictive_power,full_columns_ordered_by_predictive_power


app = Flask(__name__)
app.secret_key = 'PredictionFTW'

forest = RandomForestClassifier(n_estimators = 100)

df = pd.read_csv('data cleaning and imputing/imputed.csv', header=0)

aggregated_df = pd.read_csv('data cleaning and imputing/aggregated.csv', header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
df = df.ix[:,1:]


@app.route("/")
def index():
	websession.clear()
	total_forets_points=-1
	total_users_points=-1
	return render_template('seed_questions.html', total_users_points = total_users_points, total_forets_points=total_forets_points)


@app.route("/nextquestion", methods = ["POST"])
def display_question():
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

		# add
		playsession.add_play_session()

		#add playsession ID to websession
		websession['session_id'] = playsession.session_id

		# keep track of what question number we're on in the websession
		websession['current_q_numb'] = 0

		# set foret's points equal to 0
		websession['forets_points'] = 0

		# set user's points equalt to 0
		websession['users_points'] = 0

		print websession['users_points']
		

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
			return render_template('thank_you.html', total_forets_points = websession['forets_points'], total_users_points = websession['users_points'])

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

	# making a list of answer options tuples, and a separate list of the % of people who answered with each of those options, to hand to the html template. Pulling from reversed data dict b/c 1) can use keys to create the order, and 2) already removed NaN's from reversed data dict
	new_question_answer_list = []
	data_for_chart = []
	for i in range(len(reversed_data_dict[new_question_var_name])):
		if new_question_var_name == 'income_distribution': #doesn't have a 0 answer so need to start at 1
			new_question_answer_list.append((i+1,reversed_data_dict[new_question_var_name][i+1]))
			data_for_chart.append(int(aggregated_df[new_question_var_name][i+1]*100 + .5)) #pulling data out of aggregated file, using current var name and number of answer option. Multiplying by 100 to make them percents, adding .5 to make int round correctly.
		else:
			new_question_answer_list.append((i,reversed_data_dict[new_question_var_name][i]))
			data_for_chart.append(int(aggregated_df[new_question_var_name][i]*100 + .5)) #pulling data out of aggregated file, using current var name and number of answer option. Multiplying by 100 to make them percents, adding .5 to make int round correctly.


	websession['len_of_answer_list'] = len(new_question_answer_list)-1 # Will use this to calculate points. Minus one because if algorithm guesses exactly wrong, it should get 0 points

	total_forets_points = websession["forets_points"]
	total_users_points = websession["users_points"]

	a='a'



# clean up the below at some point - is everythin here used in template?  #TODO
	return render_template('question.html', predicted_new_question_answer = predicted_new_question_answer, predicted_new_question_translated = predicted_new_question_translated, new_question_var_name = new_question_var_name, new_question_text = new_question_text, new_question_answer_list = new_question_answer_list, new_question_title=new_question_title, question_numb = websession['current_q_numb']+1, total_users_points = total_users_points, total_forets_points = total_forets_points, test = [5,10,15,20,25,30,35], test2 = [a,a,a,a,a,a,a], data_for_chart=data_for_chart)


@app.route("/submitanswer", methods=["POST"])
def submit_answer():
	global aggregated_df

	#get submitted answers from form
	old_question_answer_numb = int(request.form.get("old_question_answer_numb"))
	guess = int(request.form.get("guess"))

	#determine what question we're on
	old_question_var_name = columns_ordered_by_predictive_power[websession['current_q_numb']]

	#pull the % of Americans who answered the same way as the responded
	percent_who_answered_same_as_guess = int(aggregated_df[old_question_var_name][old_question_answer_numb] * 100 + .5) # add .5 to make sure the int rounds correctly

	# calculate the number of points foret gets for her algorithm guess
	points_per_answer = 100/int(websession["len_of_answer_list"])
	prediction=int(websession["prediction"])
	prediction_points = 100 - abs(old_question_answer_numb - prediction)*points_per_answer #points is a function of distance between predicted answer and submitted answer, plus number of answer choices. max for each q is 100, min is 0.
	if prediction_points == 1:
		prediction_points = 0 #necessary because of weirdness with decimal places

	# calculate the number of points the respondent gets for the accuracy of their guess
	guess_points = 100 - abs(percent_who_answered_same_as_guess - guess) # points is the distance between your guess and the answer, such that a perfect guess is worth 100 points
	
	#keep track of foret's and user's total points tally
	websession["forets_points"] += prediction_points 
	total_forets_points = websession["forets_points"]
	websession["users_points"] += guess_points
	total_users_points = websession['users_points']

	#send all that data to template
	to_send = str(prediction_points)+" "+ str(total_forets_points)+" "+str(guess)+ "% " + str(percent_who_answered_same_as_guess) + "% " + str(guess_points) + " " + str(total_users_points)
	return str(to_send)

@app.route("/about")
def about():
	return render_template('about.html', total_forets_points=websession["forets_points"],total_users_points=websession['users_points'])

if __name__ == "__main__":
	app.run(debug = True)