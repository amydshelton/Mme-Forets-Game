$(document).ready(function() {
	console.log("I'm in the custom JS");
	$("#prediction_button").click(function(evt) {
		evt.preventDefault();
		$("#prediction").show();
		console.log("got here");
	});
});


// '<div id="prediction"> predicted {{new_question_var_name}} status: {{predicted_new_question_translated}} <button type="btn btn-lg btn-primary btn-block" type="submit">Submit</button> </div>');