$(document).ready(function() {

	// var guess = $("#guess");
	// guess.val(guess.val() + "more text");
	$("#prediction_button").click(function(evt) {
		evt.preventDefault();
		// $("#prediction").show();

		var old_question_answer_numb = $("input:radio[name=question]:checked").val();
		var guess = $("input[name=guess]").val();

		if (old_question_answer_numb && guess && isNaN(+guess)===false && guess >= 0 && guess <=100) {
			$.post('/submitanswer',{'old_question_answer_numb': old_question_answer_numb,'guess': guess})
			.done(function(stuff) {


				var stuff_dict = JSON.parse(stuff);


				// Update total points in top left corner
				var total_forets_points = stuff_dict.total_forets_points;
				var total_users_points = stuff_dict.total_users_points;
				$("#total_forets_points").html(total_forets_points);
				$("#total_users_points").html(total_users_points);


				// Get info needed for first message and display it in the right place
				var points_for_question = stuff_dict.prediction_points;
				var predicted_answer = stuff_dict.predicted_new_question_answer;
				var predicted_answer_id = '#'.concat(predicted_answer);
				var message = "<-- Madame Forêt predicted you would say this answer, so she gets ".concat(points_for_question, " points.");
				$(predicted_answer_id).text(message);

				chosen_radio = String(old_question_answer_numb).concat("_radio");
				document.getElementById(chosen_radio).setAttribute('class','player');

				// Get info needed for second message and display it in the right place
				var percent_who_answered_same_as_guess = stuff_dict.percent_who_answered_same_as_guess;
				var guess_points = stuff_dict.guess_points;
				var message2 = "A total of ".concat(percent_who_answered_same_as_guess, "% of Americans agree with you, so you get ", guess_points, " points.");
				$("#percent-who-agree").text(message2);

				// Disable Reval Prediction button
				$("#prediction_button").prop("disabled",true);

				$("#next-question").show();

				// Get data and labels for chart
				var data_for_chart = stuff_dict.data_for_chart;
				var labels_for_chart = stuff_dict.new_question_answer_list_for_chart;
				var length_of_chart_data = data_for_chart.length;

				// Color the answer that the person chose red
				var fillColorList = Array.apply(null, new Array(length_of_chart_data)).map(String.prototype.valueOf,"rgba(220,220,220,0.5)"); // make a list that is the right length, full of the gray color
				var varName = stuff_dict.old_question_var_name;
				if (varName === "income_distribution") {
					fillColorList[old_question_answer_numb-1] = "#178F01";

				} else {
					fillColorList[old_question_answer_numb] = "#178F01";
				} // color the chosen answer red (accomodate for the fact that there is no '0th' answer for income distribution)

				var max_of_chart_data = Math.max.apply(Math, data_for_chart);

				var maxScaleStep = Math.ceil(max_of_chart_data/10);




				var barChartData = {
					labels : labels_for_chart,
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
								responsive : true, scaleOverride: true, scaleStartValue: 0, scaleSteps: maxScaleStep, scaleStepWidth: 10, scaleLabel: "<%= Number(value) + '%'%>",  annotateDisplay:true, annotateLabel : "<%=v2%>: <%=v3%>%"
							};


				var ctx = document.getElementById("canvas").getContext("2d");

				window.myBar = new Chart(ctx).Bar(barChartData, options);
	

			});
		}
		else {
			alert("That is not a valid entry. Please edit and try again.");
		}
		

	});
});




