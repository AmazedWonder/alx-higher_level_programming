$(document).ready(function() {
    // Fetch character data from the URL
    $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
	// Display character name in the <div> element with ID 'character'
	$('DIV#character').text(data.name);
    });
});
