from flask import Flask, render_template, request, session as websession
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
	websession.clear()
	return render_template('seed_questions.html')


@app.route("/nextquestion", methods = ["POST"])
def display_question():
	global data_dict, reversed_data_dict, forest, df

	## if starting a new game:
	if 'session_id' not in websession:

		#get out of the form the items put in
		age = int(request.form.get("age"))
		sex = data_dict['sex']['answers'][str(request.form.get("sex"))]
		race = data_dict['race']['answers'][str(request.form.get("race"))]
		region = data_dict['region']['answers'][str(request.form.get("region"))]
		highest_grade = int(request.form.get("highest-grade"))
		employment_status = data_dict['employment_status']['answers'][str(request.form.get("employment-status"))]
		marital_status = data_dict['marital_status']['answers'][str(request.form.get("marital-status"))]

		#this will be the data the model uses to predict the answer to the next question
		test_data = [age, sex, race, region, highest_grade, employment_status, marital_status]

		# variable name is the first one in the order of questions
		new_question_var_name = column_order[0]	

		# instantiate playsession
		playsession = PlaySession(age = age, sex = sex, race = race, region = region, highest_grade = highest_grade, employment_status = employment_status, marital_status = marital_status)

		# add and commit
		playsession.add_play_session()

		#add playsession ID to websession
		websession['session_id'] = playsession.session_id

		# keep track of what question number we're on in the websession
		websession['current_q_numb'] = 0
		

	#continuing an existing game
	else:

		# get name of the last question answered from web session
		old_question_var_name = column_order[websession['current_q_numb']]

		#get whatever they answered out of the form
		old_question_answer = data_dict[old_question_var_name]['answers'][str(request.form.get(old_question_var_name))]
		

		# Get current playsession object out of database, using id stored in websession
		playsession = dbsession.query(PlaySession).get(websession['session_id'])

		# attach what they just submitted to playsession object
		setattr(playsession, old_question_var_name, old_question_answer)

		# up the cound of the current question
		websession['current_q_numb'] += 1

		#if the last question submitted is the last one on in the list of questions (aka #22 ), then commit the playsession and render the thank you template
		if column_order.index(old_question_var_name) == 22:
			playsession.commit_play_session()
			return render_template('thank_you.html')

		#if it's not the last question, determine what the next question is and set up the test data
		else:
			new_question_var_name = column_order[websession['current_q_numb']]
			test_data = playsession.ordered_parameter() 


	column_of_var = column_order.index(new_question_var_name) + 8 #because there are 7 demographic questions before the predictable questions begin, and we need to slice up to current column plus one b/c range of slice is not inclusive

	### Set up training data ###
	train_data = df.ix[:,0:column_of_var] #trimming it down to just the columns up to and including the target variable
	train_data_values = train_data.values #converting out of dataframe
	features_of_training_data = train_data_values[0::,0:-1:] #whole dataset minus last column, which is target variable
	target_variable = train_data_values[0::,-1] # slices off the last column, which is the target variable 

	# Fit the training data to the target and create the decision trees
	forest = forest.fit(features_of_training_data, target_variable)

	
	predicted_new_question_answer = forest.predict(test_data)[0] #comes back as a one-item list.  sliced it down to a single number

	# add stated old question answer and predicted new question answer to database, then commit
	predicted_new_question_var_name = "predicted_"+str(new_question_var_name)
	setattr(playsession, predicted_new_question_var_name, predicted_new_question_answer)
	playsession.commit_play_session()

	predicted_new_question_translated = reversed_data_dict[new_question_var_name][int(predicted_new_question_answer)]


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