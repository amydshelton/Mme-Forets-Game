$(document).ready(function() {

    $("#submit").click(function(evt) {

        // On first page, on submit, check to see if age is a number. 
        // If it is not, alert user with error
        var age = $("input[name=age]").val();
        if (isNaN(+age)) {
            alert("Your age must be a number.");
            evt.preventDefault();

        }
    });

    $("#prediction_button").click(function(evt) {

        // Reveal prediction and update Mme. Foret's points

        evt.preventDefault();

        // Get answer out of form
        var old_question_answer_numb = $("input:radio[name=question]:checked"
                                        ).val();

        // If they did select something, add it the dictionary that gets handed 
        // back to the python master file
        if (old_question_answer_numb) {
            $.post('/submitfirstanswer',{'old_question_answer_numb':
                                          old_question_answer_numb})

            // After dictionary has been handed to master.py, master.py will 
            // hand back a JSON dictionary of info needed (dictionary is 
            // elegantly named 'stuff' :D )
            .done(function(stuff) {
                var stuff_dict = JSON.parse(stuff);

                // Get info needed for first message and display it in the right
                // place
                var points_for_question = stuff_dict.prediction_points;
                var predicted_answer = stuff_dict.predicted_new_question_answer;
                var predicted_answer_id = '#'.concat(predicted_answer);
                var message = "<-- Madame Forêt predicted you would say this " +
                                "answer, so she gets ".concat(
                                points_for_question, " points.");
                $(predicted_answer_id).text(message);

                // Update total points in top right corner
                var total_forets_points = stuff_dict.total_forets_points;
                $("#total_forets_points").html(total_forets_points);

                // Disable Guess Prediction button
                $("#prediction_button").prop("disabled",true);

                // Reveal second question
                $("#second-question").show();

                // Reveal Mme. Foret's points (only matters on first page b/c 
                // of jinja syntax on HTML page)
                $("#forets_words").removeClass("hidden-on-first-page");

            });
        }
        // This alert shows if they tried to hit 'reveal' without choosing an 
        // option first
        else {
            alert("Please select an answer.");
        }
    });
    

    $("#guess_button").click(function(evt) {

        // Reveal how accurate player's guess was, determine points, show chart,
        // reveal 'next question' button

        evt.preventDefault();

        // Get info out of form 
        var old_question_answer_numb =
                                $("input:radio[name=question]:checked").val();
        var guess = $("input[name=guess]").val();

        // Check to make sure they answered both questions and that the guess 
        // submitted is a number between 0 and 100
        if (old_question_answer_numb && guess && isNaN(+guess)===false &&
            guess >= 0 && guess <=100) {

            // Put the submitted answers into a dictionary to hand back to 
            // master.py
            $.post('/submitsecondanswer',{'old_question_answer_numb':
                old_question_answer_numb,'guess': guess})

            // After dictionary has been handed to master.py, master.py will 
            // hand back a JSON dictionary (called stuff!) full of info needed 
            // for function below.
            .done(function(stuff) {

                var stuff_dict = JSON.parse(stuff);

                // Update total points in top left corner
                var total_players_points = stuff_dict.total_players_points;
                $("#total_players_points").html(total_players_points);

                // Add the 'player' class to the chosen radio to make it turn 
                // green
                chosen_radio = String(old_question_answer_numb).
                                      concat("_label");
                document.getElementById(chosen_radio).setAttribute('class',
                                                                   'player');

                // Get info needed for second message and display it in the 
                // right place
                var percent_who_answered_same_as_player =
                                stuff_dict.percent_who_answered_same_as_player;
                var player_points = stuff_dict.player_points;
                var message2 = "A total of ".concat(
                    percent_who_answered_same_as_player, "% of Americans agree"+
                           " with you, so you get ", player_points, " points.");
                $("#percent-who-agree").text(message2);

                // Disable Reveal Prediction button
                $("#guess_button").prop("disabled",true);

                // Reveal 'Next Question' button
                $("#next-question").show();

                // Reveal player's points (only matters on first page b/c of 
                // jinja syntax on HTML page)
                $("#players_words").removeClass("hidden-on-first-page");


                // Color the bar of answer that the person chose green in the 
                // chart
                var length_of_chart_data = stuff_dict.data_for_chart.length;
                var fillColorList = Array.apply(null, new Array
                        (length_of_chart_data)).map(String.prototype.valueOf,
                        "rgba(220,220,220,0.5)");
                        // make a list that is the right length, full of the 
                        // gray color
                var varName = stuff_dict.old_question_var_name;
                if (varName === "income_distribution") {
                    fillColorList[old_question_answer_numb-1] = "#178F01";

                } else {
                    fillColorList[old_question_answer_numb] = "#178F01";
                } // color the chosen answer green (accomodate for the fact 
                    // that there is no '0th' answer for income distribution)

                // Determine what the max of the y axis should be
                var max_of_chart_data = Math.max.apply(Math,
                    stuff_dict.data_for_chart);
                var maxScaleStep = Math.ceil(max_of_chart_data/10);

                // Dictionary of what the labels for the charts should be
                var labels_for_charts = {
                    'religious':
                        ['Not\nReligious', 'Slightly\nReligious',
                        'Moderately\nReligious', 'Very\nReligious'],
                    'spiritual':
                        ['Not\nSpiritual', 'Slightly\nSpiritual',
                        'Moderately\nSpirtual', 'Very\nSpiritual'],
                    'party':
                        ['Strong\nRep.', 'Not\nStrong\nRep.',
                        'Ind.,\nNear\nRep.', 'Ind.', 'Ind.,\nNear\nDem.',
                        'Not\nStrong\nDem.', 'Strong\nDem.'],
                    'death_penalty':
                        ['Oppose', 'Favor'],
                    'court_harsh':
                        ['Not Harsh\nEnough', 'About Right', 'Too Harsh'],
                    'bar':
                        ['Never', 'Once\na Year', 'Several\nTimes\na Year',
                        'Once\na Month', 'Several\nTimes\na Month',
                        'Several\nTimes\na Week', 'Almost\nDaily'],
                    'tv':
                        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9 to 12',
                        '13 or\nhigher'],
                    'relatives':
                        ['Never', 'Once\na Year', 'Several\nTimes\na Year',
                        'Once\na Month', 'Several\nTimes\na Month',
                        'Several\nTimes\na Week', 'Almost\nDaily'],
                    'spanking':
                        ['Strongly\nDisagree', 'Disagree', 'Agree',
                        'Strongly\nAgree'],
                    'income_distribution':
                        ['1', '2', '3', '4', '5', '6', '7'],
                    'standard_of_living':
                        ['Much\nWorse', 'Somewhat\nWorse', 'About\nthe Same',
                        'Somewhat\nBetter', 'Much\nBetter'],
                    'birth_control':
                        ['Strongly\nDisagree', 'Disagree', 'Agree',
                        'Strongly\nAgree'],
                    'immigration':
                        ['Reduced\na Lot', 'Reduced\na Little',
                        'Remain\nthe Same\nas It Is', 'Increased\na Little',
                        'Increased\na Lot'],
                    'affirmative_action':
                        ['Strongly\nOppose\nPreference\nfor Afr.\nAmericans',
                        'Oppose\nPreference\nfor Afr.\nAmericans',
                        'Support\nPreference\nfor Afr.\nAmericans',
                        'Strongly\nSupport\nPreference\nfor Afr.\nAmericans'],
                    'gun':
                        ['No','Yes'],
                    'tax_approp':
                        ['Too Low', 'About Right','Too High'],
                    'divorce_ease':
                        ['Easier', 'Stay Same', 'More Difficult'],
                    'numb_children':
                        ['None', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                        'Seven\nor more']
                    };

                // Feed in data to make the chart
                var barChartData = {
                    labels : labels_for_charts[varName],
                    datasets : [
                        {
                            fillColor : fillColorList,
                            strokeColor : "rgba(220,220,220,0.8)",
                            highlightFill: "rgba(220,220,220,0.75)",
                            highlightStroke: "rgba(220,220,220,1)",
                            data : stuff_dict.data_for_chart
                        },
                    ]

                }, options = {
                                responsive : true,
                                scaleOverride: true,
                                scaleStartValue: 0,
                                scaleSteps: maxScaleStep,
                                scaleStepWidth: 10,
                                scaleLabel: "<%= Number(value) + '%'%>",
                                annotateDisplay:true,
                                annotateLabel : "<%=v2%>: <%=v3%>%",
                                graphTitle : "Responses of Surveyed Americans",
                                yAxisLabel: "Percent of Respondents"
                            };

                // Make the chart
                var ctx = document.getElementById("canvas").getContext("2d");
                window.myBar = new Chart(ctx).Bar(barChartData, options);
    

            });
        }
        else {
            alert("That is not a valid entry. Please edit and try again.");
        }
        

    });
});




