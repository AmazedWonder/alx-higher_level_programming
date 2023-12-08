$(document).ready(function() {
    $('#btn_translate').click(fetchTranslatn);
    $('#language_code').keypress(function(event) {
	if (event.keyCode === 13) {
	    fetchTranslatn();
	}
    });

    function fetchTranslatn() {
	const languageCode = $('#language_code').val();
	const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

	$.get(apiUrl, function(data) {
	    $('#hello').text(data.hello);
	});
    }
});
