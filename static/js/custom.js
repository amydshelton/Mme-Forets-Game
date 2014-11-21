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
				var stuff_list = stuff.split(" ");
				var guess = stuff_list.slice(2,3);




				// Update total points in top left corner
				var total_forets_points = stuff_list.slice(1,2);
				var total_users_points = stuff_list.slice(5,6);
				$("#total_forets_points").html(total_forets_points);
				$("#total_users_points").html(total_users_points);


				// Get info needed for first message and display it in the right place
				var points_for_question = stuff_list.slice(0,1);
				var predicted_answer = Math.round(document.getElementById("predicted-answer").innerHTML);
				var predicted_answer_id = '#'.concat(predicted_answer);
				var message = "<-- Madame Forêt predicted you would say this answer, so she gets ".concat(points_for_question, " points.");
				$(predicted_answer_id).text(message);

				// Get info needed for second message and display it in the right place
				var percent_who_answered_same_as_guess = stuff_list.slice(3,4);
				var guess_points = stuff_list.slice(4,5);
				var message2 = "   A total of ".concat(percent_who_answered_same_as_guess, " of Americans agree with you, so you get ", guess_points, " points.");
				$("#percent-who-agree").text(message2);

				// Disable Reval Prediction button
				$("#prediction_button").prop("disabled",true);

				$("#next-question").show();
				// $("#chart").show();

				var ctx = document.getElementById("canvas").getContext("2d");
				window.myBar = new Chart(ctx).Bar(barChartData, {
					responsive : true
				});
	

			});
		}
		else {
			alert("That is not a valid entry. Please edit and try again.");
		}
		

	});
});





// '<div id="prediction"> predicted {{new_question_var_name}} status: {{predicted_new_question_translated}} <button type="btn btn-lg btn-primary btn-block" type="submit">Submit</button> </div>');