from flask import Flask, render_template, redirect, request, session as websession

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
	print age, sex, race, region, highest_grade
	return render_template('first_question.html', age = age, sex = sex, race = race, region = region, highest_grade = highest_grade)

if __name__ == "__main__":
    app.run(debug = True)