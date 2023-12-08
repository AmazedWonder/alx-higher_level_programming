$(document).ready(function() {
    // Fetch data from the URL
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
	// Display the value of "hello" in the <div> element with ID 'hello'
	$('DIV#hello').text(data.hello);
    });
});
