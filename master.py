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
		employment_status = data_dict['employment_status']['answers'][str(request.form.get("employment-status"))]
		marital_status = data_dict['marital_status']['answers'][str(request.form.get("marital-status"))]
		highest_grade = int(request.form.get("highest-grade"))		

		# convert categoricals into booleans - start them as zero
		dict_categoricals = { 
			'race': 
				{'american_indian':0, 'asian_indian':0, 'black':0, 'chinese':0, 'filipino':0, 'hispanic':0, 'japanese':0, 'korean':0,'multiple':0, 'hawaiian':0, 'asian':0, 'pacific_islander':0, 'samoan':0, 'other_race':0, 'vietnamese':0, 'white':0}, 
			'region': 
				{'east_north_central':0, 'east_south_central':0, 'middle_atlantic':0, 'mountain':0, 'new_england':0, 'pacific':0, 'south_atlantic':0, 'west_north_central':0, 'west_south_central':0},
			'employment_status':
				{'keeping_house':0, 'other_employment':0, 'retired':0,'school':0, 'temp_not_working':0, 'unemployed':0,'fulltime':0,'parttime':0},
			'marital_status':
				{'divorced':0, 'married':0, 'never_married':0, 'separated':0, 'widowed':0},
		}

		# update appropriate boolean to 1
		dict_categoricals['race'][race] = 1
		dict_categoricals['region'][region]=1
		dict_categoricals['employment_status'][employment_status]=1
		dict_categoricals['marital_status'][marital_status]=1

		# set variables equal to what's in dictionary
		american_indian = dict_categoricals['race']['american_indian']
		asian_indian = dict_categoricals['race']['asian_indian']
		black = dict_categoricals['race']['black']
		chinese = dict_categoricals['race']['chinese']
		filipino = dict_categoricals['race']['filipino']
		hispanic = dict_categoricals['race']['hispanic']
		japanese = dict_categoricals['race']['japanese']
		korean = dict_categoricals['race']['korean']
		multiple = dict_categoricals['race']['multiple']
		hawaiian = dict_categoricals['race']['hawaiian']
		asian = dict_categoricals['race']['asian']
		pacific_islander = dict_categoricals['race']['pacific_islander']
		samoan = dict_categoricals['race']['samoan']
		other_race = dict_categoricals['race']['other_race']
		vietnamese = dict_categoricals['race']['vietnamese']
		white = dict_categoricals['race']['white']
		east_north_central = dict_categoricals['region']['east_north_central']
		east_south_central = dict_categoricals['region']['east_south_central']
		middle_atlantic = dict_categoricals['region']['middle_atlantic']
		mountain = dict_categoricals['region']['mountain']
		new_england = dict_categoricals['region']['new_england']
		pacific = dict_categoricals['region']['pacific']
		south_atlantic = dict_categoricals['region']['south_atlantic']
		west_north_central = dict_categoricals['region']['west_north_central']
		west_south_central = dict_categoricals['region']['west_south_central']
		keeping_house = dict_categoricals['employment_status']['keeping_house']
		other_employment = dict_categoricals['employment_status']['other_employment']
		retired = dict_categoricals['employment_status']['retired']
		school = dict_categoricals['employment_status']['school']
		temp_not_working = dict_categoricals['employment_status']['temp_not_working']
		unemployed = dict_categoricals['employment_status']['unemployed']
		fulltime = dict_categoricals['employment_status']['fulltime']
		parttime = dict_categoricals['employment_status']['parttime']
		divorced = dict_categoricals['marital_status']['divorced']
		married = dict_categoricals['marital_status']['married']
		never_married = dict_categoricals['marital_status']['never_married']
		separated = dict_categoricals['marital_status']['separated']
		widowed = dict_categoricals['marital_status']['widowed']


		#this will be the data the model uses to predict the answer to the next question
		test_data = [age, sex, american_indian, asian_indian, black, chinese, filipino, hispanic, japanese, korean, multiple, hawaiian, asian, pacific_islander, samoan, other_race, vietnamese, white, east_north_central, east_south_central, middle_atlantic, mountain, new_england, pacific, south_atlantic, west_north_central, west_south_central, keeping_house, other_employment, retired, school, temp_not_working, unemployed, fulltime, parttime, divorced, married, never_married, separated, widowed, highest_grade]

		# variable name is the first one in the order of questions
		new_question_var_name = column_order[0]	

		# instantiate playsession
		playsession = PlaySession(age = age, sex = sex, american_indian = american_indian, asian_indian = asian_indian, black = black, chinese = chinese, filipino = filipino, hispanic = hispanic, japanese = japanese, korean = korean, multiple = multiple, hawaiian = hawaiian, asian = asian, pacific_islander = pacific_islander, samoan = samoan, other_race = other_race, vietnamese = vietnamese, white = white, east_north_central = east_north_central, east_south_central = east_south_central, middle_atlantic = middle_atlantic, mountain = mountain, new_england = new_england, pacific = pacific, south_atlantic = south_atlantic, west_north_central = west_north_central, west_south_central = west_south_central, keeping_house = keeping_house, other_employment = other_employment, retired = retired, school = school, temp_not_working = temp_not_working, unemployed = unemployed, fulltime = fulltime, parttime = parttime, divorced = divorced, married = married, never_married = never_married, separated = separated, widowed = widowed, highest_grade = highest_grade)

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
		old_question_var_name = column_order[websession['current_q_numb']]

		#get whatever they answered out of the form
		old_question_answer = request.form.get("question")
		

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


	column_of_var = column_order.index(new_question_var_name) + 42 #because there are 41 demographic questions before the predictable questions begin, and we need to slice up to current column plus one b/c range of slice is not inclusive

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

	# making a list of answer options to hand to the html template. Pulling form reversed data dict b/c 1) can use keys to create the order, and 2) already removed NaN's from reversed data dict
	new_question_answer_list = []
	for i in range(len(reversed_data_dict[new_question_var_name])):
		questions_without_0_answer = ['income_distribution','govt_help_poor','govt_help_sick','govt_more_less','govt_help_blacks']
		if new_question_var_name in questions_without_0_answer:
			new_question_answer_list.append((i+1,reversed_data_dict[new_question_var_name][i+1]))
		else:
			new_question_answer_list.append((i,reversed_data_dict[new_question_var_name][i]))

	websession['len_of_answer_list'] = len(new_question_answer_list)-1 # Will use this to calculate points. Minus one because if algorithm guesses exactly wrong, it should get 0 points

	return render_template('question_test.html', predicted_new_question_translated = predicted_new_question_translated, new_question_var_name = new_question_var_name, new_question_text = new_question_text, new_question_answer_list = new_question_answer_list, new_question_title=new_question_title, question_numb = websession['current_q_numb']+1)


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