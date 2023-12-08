$(document).ready(function() {
    // Add a click event listener to the <div> element with ID 'toggle_header'
    $('div#toggle_header').click(function() {
	// Toggle the class of the <header> element
	$('header').toggleClass('red green');
    });
});
