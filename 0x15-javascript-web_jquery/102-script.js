$(document).ready(function() {
    // adds event listener for the translate button
    $('input#btn_translate').click(function() {
	// makes API request to fetch the translation
	$.get('https://www.fourtonfish.com/hellosalut/hello/' + $('input#language_code').val(), function(data) {
	    // displays the translation in the hello div
	    $('div#hello').text(data.hello);
	});
    });
});
