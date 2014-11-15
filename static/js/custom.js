$(document).ready(function() {
	$("#prediction_button").click(function(evt) {
		evt.preventDefault();
		$("#prediction").show();
		$.post('/submitanswer',{old_question_answer_numb:$("input:radio[name=question]:checked").val()})
			.done(function(data) {
				console.log("points: "+data);
				$("#points").html(data);
			});

	});
});


// '<div id="prediction"> predicted {{new_question_var_name}} status: {{predicted_new_question_translated}} <button type="btn btn-lg btn-primary btn-block" type="submit">Submit</button> </div>');