$(document).ready(function() {
    // adds event listener to add a new element
    $('div#add_item').click(function() {
	// Create a new <li> element with the text 'Item'
	$('<li>').text('Item').appendTo('ul.my_list');
    });

    // adds event listener to remove the last element
    $('div#remove_item').click(function() {
	// selects the last <li> element in the list and remove it
	$('ul.my_list li:last-child').remove();
    });

    // adds event listener for clearing the list
    $('div#clear_list').click(function() {
	// removes all <li> elements from the list
	$('ul.my_list').empty();
    });
});
