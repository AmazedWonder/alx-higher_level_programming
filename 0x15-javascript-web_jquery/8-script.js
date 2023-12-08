$(document).ready(function() {
    // fetch movie data from the URL
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	// iterates over each movie and create a list item for its title
	$.each(data.results, function(index, movie) {
	    // create a new list item with the movie title
	    $('<li>').text(movie.title).appendTo('ul#list_movies');
	});
    });
});
