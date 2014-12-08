Madame Forêt's Game
===============
Play Madame Forêt's Game, where you compete against a "psychic" (aka a machine 
learning algorithm) by answering questions about yourself and the American 
public. Madame Forêt predicts what you will answer, while you guess what 
percentage of Americans agree with you. Both of you get points for the accuracy 
of your guesses.

Madame Forêt's Game was built by 
    <a href="http://amydshelton.com">Amy Shelton</a> 
in November 2013, as her independent project for 
    <a href="http://www.hackbrightacademy.com/">Hackbright Academy</a>.

This readme is divided into three main sections: The User Experience, Behind 
the Scenes, and About Amy. 



##The User Experience

###Playing the Game
After sharing their age and the highest grade they've completed, players answer 
a question from the 
    <a href="http://en.wikipedia.org/wiki/General_Social_Survey">
        General Social Survey</a>. 
Then they click a button to reveal how Madame Forêt predicted the player would 
answer.  Madame Forêt receives points for her answer (ranging from a min. of 0 
to a max. of 100), depending on how accurate the answer was). The player then 
guesses what percentage of Americans would have also selected the same answer 
they chose. Then they click a button to reveal how accurate their guess was, 
and to reveal a chart showing the distibution of responses. They also receive 
points for their answer, again ranging from 0 to 100. Then they move on to the 
next question and the process repeats itself.
![](https://github.com/amydshelton/Mme-Forets-Game/blob/master/static/img/for_github_readme/User_experience.gif?raw=true "Playing the Game")

As Madame Forêt learns more about the player, her prediction model gets refined 
and becomes more accurate.

###Other Pages
The main page of the game is explained in detail above. The app also includes a 
scoreboard, which shows the top 10 scores of all time. (Individuals who score 
in the top 10 will be asked to sign the scoreboard upon completing the game.) 
In addition, the app has a front page, an about page, a congrats-you-won page, 
a sorry-you-lost page, and an it's-a-tie page. 


##Behind the scenes

###Technologies Used
This app includes the following technologies:<ul>
<li>Python</li>
<li><a href="http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.
             RandomForestClassifier.html">Scikit-learn</a></li>
<li>Pandas</li>
<li>Flask</li>
<li>Sqlite3</li>
<li>Sqlalchemy</li>
<li>Javascript</li>
<li><a href="https://github.com/FVANCOP/ChartNew.js/">ChartNew.JS</a></li>
<li>HTML</li>
<li>CSS</li>
<li>Bootstrap</li>
</ul>

###Structure of Files
The main files of Madame Forêt's Game are as follows:<ul>
    <li>```model.py```: This file creates the database and defines the 
        ```PlaySession``` class and the ```RandomForest``` class that map to 
        the database tables.</li>
    <li>```cache_rf_models.py```: This file stores the Random Forest models 
        for each of the 18 questions.</li>
    <li>```master.py```: This is the heart of the app. It calls the cached 
        Random Forest models to predicts answers, updates the database, and 
        feeds information to the front end.</li>
    <li>```custom.js```: This file (saved in ```static/js```) controls the 
        front end. It has event listeners to reveal buttons, charts, and 
        predictions.</li>
    <li>```universals.py```: This contains dictionaries and lists accessed 
        by other files, such as a list with the order that questions should be 
        revealed.</li>
    <li>```Mme_Forets_Game.db```: This is the sqlite3 database for the app. It 
        is not included in this repository, but the files to set up a similar 
        database are included here (```model.py``` and 
        ```cache_rf_models.py```).
    <li>**CSS files:** These files (saved in the ```static``` folder) control 
        the styling of the HTML pages. </li>
    <li>**HTML templates:** These files (saved in the ```templates``` folder) 
        are the pages of the app.</li>
    <li>**GSS data files:** These files (saved in the ```GSS``` folder) contain 
        the original, raw data.</li>
    <li>**Cleaning and imputing files:** The python files (saved in the 
        ```data cleaning and imputing```) file were used to clean and impute 
        the raw data. Please see the Data Prep section (below) for more 
        information.
    <li>**Feature testing files:** These files (saved in the 
        ```feature_testing``` folder) were used to help understand which 
        questions (aka features) are most predictive. They are not necessary 
        for the app to work.</li>
</ul>

###How to Install Madame Forêt's Game on Your Machine
Follow these steps to install Madame Forêt's Game:
<ol>
    <li>Create a dedicated folder on your machine.</li>
    <li>In terminal, navigate into that folder and create and activate a 
        <a href="http://virtualenv.readthedocs.org/en/latest/virtualenv.html">
            virtual environment</a>.</li>
    <li>Install the required packages. To do so, from your terminal, type: <br>
        ```pip install -r requirements.txt``` and hit Enter.</li>
    <li>From terminal, type: <br>
        ```python model.py``` and hit Enter. This sets up your database.</li>
    <li>In terminal, type ```python cache_rf_models.py``` and hit Enter. This 
        will make and cache (aka pickle) the random forest model for each 
        question. The models are saved in the random_forest table of your 
        database.</li>
    <li>In terminal, type ```python master.py``` and hit Enter. This will start 
        the server.</li>
    <li>Navigate to <a href="localhost:5000/">localhost:5000</a> and play!</li>
</ol>

###Data Prep
If you want to replicate the steps I took to prepare the data, they are 
outlined here. The final product of these steps - the file named 
```imputed.csv``` - is included in this repository, so if you would like to 
skip these steps when running Madame Forêt's Game on your machine, you can.
<ol>
<li>Open the full, raw data from the General Social Survey. That data is 
    included in this repository (```GSS/GSS Data for Statwing Prize (1).csv```) 
    or can be downloaded from 
    <a href="http://blog.statwing.com/open-data-the-general-social-survey-40-
    years-of-results/">
    Statwing's website</a>. Save it in a subfolder called ```GSS```.</li> 
<li>Edit the file down to the years (2008, 2010, and 2012) and the 18 variables 
    of interest (which are listed in ```universals.py```), and save the 
    resulting file as ```GSS/2008, 2010, and 2012 results for variables of 
    interest.csv``` .</li>
<li>In terminal, navigate to the ```data cleaning and imputing``` folder. Make 
    sure your virtual environment is active. Type:<br>
```python cleaning_data.py``` then hit Enter.</li>
<li>You should now have a file called ```cleaned.csv``` with integers in place 
    of strings. However, this file still has missing data. Therefore, we'll use 
    Random Forest to impute the missing data. In terminal, type:<br>
```python imputing_data.py``` then hit Enter.</li>

<p>The resulting file, imputed.csv, is read into ```master.py```.</p>

###The Prediction Algorithm - Random Forest
"Madame Forêt" is powered by 
    <a href="http://scikit-learn.org/stable/modules/generated/sklearn.
             ensemble.RandomForestClassifier.html">the Random Forest algorithm 
             from scikit-learn</a>. 
The 
    <a href="http://en.wikipedia.org/wiki/Random_forest">Random Forest 
        algorithm</a> 
creates many <a href="http://en.wikipedia.org/wiki/Decision_tree">
    decision trees</a>, 
and then returns the most commonly created tree - hence the term "forest". 
The random part of the title comes from the fact that the decision trees are 
modeled with some forced random decisions, which helps prevent overfitting. 
Random Forest is an excellent algorithm for 
    <a href="http://strataconf.com/strata2012/public/schedule/
             detail/22658">predictions based on supervised learning</a>, 
and often wins <a href="https://www.kaggle.com/wiki/RandomForests">Kaggle</a> 
competitions. 

##About Amy
<a href="http://amydshelton.com">Amy</a> is a longtime numbers nerd who has a 
newfound passion for backend programming and data engineering. After 
Hackbright, she'll be looking for a job in San Francisco. 
You should probably hire her.
