$(document).ready(function() {

	$("#submit").click(function(evt) {
		var age = $("input[name=age]").val();
		if (isNaN(+age)) {
			alert("Your age must be a number.");
			evt.preventDefault();

		}
	});

	$("#prediction_button").click(function(evt) {
		evt.preventDefault();

		var old_question_answer_numb = $("input:radio[name=question]:checked").val();

		if (old_question_answer_numb) {
			$.post('/submitfirstanswer',{'old_question_answer_numb': old_question_answer_numb})
			.done(function(stuff) {
				var stuff_dict = JSON.parse(stuff);

				// Get info needed for first message and display it in the right place
				var points_for_question = stuff_dict.prediction_points;
				var predicted_answer = stuff_dict.predicted_new_question_answer;
				var predicted_answer_id = '#'.concat(predicted_answer);
				var message = "<-- Madame Forêt predicted you would say this answer, so she gets ".concat(points_for_question, " points.");
				$(predicted_answer_id).text(message);

				// Update total points in top left corner
				var total_forets_points = stuff_dict.total_forets_points;
				$("#total_forets_points").html(total_forets_points);

				// Disable Guess Prediction button
				$("#prediction_button").prop("disabled",true);

				$("#second-question").show();

			});
		}
		else {
			alert("Please select an answer.");
		}
	});
	

	$("#guess_button").click(function(evt) {
		evt.preventDefault();

		var old_question_answer_numb = $("input:radio[name=question]:checked").val();
		var guess = $("input[name=guess]").val();

		if (old_question_answer_numb && guess && isNaN(+guess)===false && guess >= 0 && guess <=100) {
			$.post('/submitsecondanswer',{'old_question_answer_numb': old_question_answer_numb,'guess': guess})
			.done(function(stuff) {

				var stuff_dict = JSON.parse(stuff);

				// Update total points in top left corner
				var total_users_points = stuff_dict.total_users_points;
				$("#total_users_points").html(total_users_points);

				chosen_radio = String(old_question_answer_numb).concat("_label");
				document.getElementById(chosen_radio).setAttribute('class','player');

				// Get info needed for second message and display it in the right place
				var percent_who_answered_same_as_guess = stuff_dict.percent_who_answered_same_as_guess;
				var guess_points = stuff_dict.guess_points;
				var message2 = "A total of ".concat(percent_who_answered_same_as_guess, "% of Americans agree with you, so you get ", guess_points, " points.");
				$("#percent-who-agree").text(message2);

				// Disable Reval Prediction button
				$("#guess_button").prop("disabled",true);

				$("#next-question").show();

				// Get data and labels for chart
				var data_for_chart = stuff_dict.data_for_chart;
				var labels_for_chart = stuff_dict.new_question_answer_list_for_chart;
				var length_of_chart_data = data_for_chart.length;

				// Color the answer that the person chose green
				var fillColorList = Array.apply(null, new Array(length_of_chart_data)).map(String.prototype.valueOf,"rgba(220,220,220,0.5)"); // make a list that is the right length, full of the gray color
				var varName = stuff_dict.old_question_var_name;
				if (varName === "income_distribution") {
					fillColorList[old_question_answer_numb-1] = "#178F01";

				} else {
					fillColorList[old_question_answer_numb] = "#178F01";
				} // color the chosen answer red (accomodate for the fact that there is no '0th' answer for income distribution)

				// Determine what the max of the y axis should be
				var max_of_chart_data = Math.max.apply(Math, data_for_chart);
				var maxScaleStep = Math.ceil(max_of_chart_data/10);

				// Determine what the labels for the charts should be
				var labels_for_charts = {
										'religious':
											['Not\nReligious', 'Slightly\nReligious', 'Moderately\nReligious', 'Very\nReligious'],
										'spiritual':
											['Not\nSpiritual','Slightly\nSpiritual', 'Moderately\nSpirtual', 'Very\nSpiritual'],
										'party':
											['Strong\nRep.', 'Not\nStrong\nRep.', 'Ind.,\nNear\nRep.', 'Ind.', 'Ind.,\nNear\nDem.', 'Not\nStrong\nDem.', 'Strong\nDem.'],
										'death_penalty':
											['Oppose','Favor'],
										'court_harsh':
											['Not Harsh\nEnough', 'About Right', 'Too Harsh'],
										'bar':
											['Never', 'Once\na Year', 'Several\nTimes\na Year', 'Once\na Month','Several\nTimes\na Month', 'Several\nTimes\na Week', 'Almost\nDaily'],
										'tv':
											['0','1', '2', '3', '4', '5', '6', '7', '8', '9 to 12', '13 or\nhigher'],
										'relatives':
											['Never', 'Once\na Year', 'Several\nTimes\na Year', 'Once\na Month','Several\nTimes\na Month', 'Several\nTimes\na Week', 'Almost\nDaily'],
										'spanking':
											['Strongly\nDisagree','Disagree','Agree','Strongly\nAgree'],
										'income_distribution':
											['1', '2', '3', '4', '5', '6', '7'],
										'standard_of_living':
											['Much\nWorse', 'Somewhat\nWorse', 'About\nthe Same','Somewhat\nBetter','Much\nBetter'],
										'birth_control':
											['Strongly\nDisagree','Disagree','Agree','Strongly\nAgree'],
										'immigration':
											['Reduced\na Lot','Reduced\na Little','Remain\nthe Same\nas It Is','Increased\na Little','Increased\na Lot'],
										'affirmative_action':
											['Strongly\nOppose\nPreference\nfor Afr.\nAmericans', 'Oppose\nPreference\nfor Afr.\nAmericans', 'Support\nPreference\nfor Afr.\nAmericans', 'Strongly\nSupport\nPreference\nfor Afr.\nAmericans'],
										'gun':
											['No','Yes'],
										'tax_approp':
											['Too Low', 'About Right','Too High'],
										'divorce_ease':
											['Easier', 'Stay Same', 'More Difficult'],
										'numb_children':
											['None', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven\nor more']
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
							data : data_for_chart
						},
					]

				}, options = {
								responsive : true, scaleOverride: true, scaleStartValue: 0, scaleSteps: maxScaleStep, scaleStepWidth: 10, scaleLabel: "<%= Number(value) + '%'%>",  annotateDisplay:true, annotateLabel : "<%=v2%>: <%=v3%>%", graphTitle : "Responses of Surveyed Americans", yAxisLabel: "Percent of Respondents"
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




