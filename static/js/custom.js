$(document).ready(function() {
	$("#prediction_button").click(function(evt) {
		evt.preventDefault();
		$("#prediction").show();

		$.post('/submitanswer',{old_question_answer_numb:$("input:radio[name=question]:checked").val(),guess:$("input[name=guess]").val()})
			.done(function(stuff) {
				console.log(stuff);
				var stuff_list = stuff.split(" ");
				var points_for_question = stuff_list.slice(0,1);
				var total_points = stuff_list.slice(1,2);
				var guess = stuff_list.slice(2,3);
				console.log(stuff_list);
				$("#points").html(points_for_question);
				$("#total_points").html(total_points);
				$("#submitted_guess").html(guess);
				$("#prediction_button").prop("disabled",true);
			});

	});
});


// '<div id="prediction"> predicted {{new_question_var_name}} status: {{predicted_new_question_translated}} <button type="btn btn-lg btn-primary btn-block" type="submit">Submit</button> </div>');