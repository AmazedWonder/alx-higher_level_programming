$(document).ready(function() {
    // Add a click event listener to the <div> element with ID 'update_header'
    $('div#update_header').click(function() {
	// Update the text of the <header> element to 'New Header!!!'
	$('header').text('New Header!!!');
    });
});
