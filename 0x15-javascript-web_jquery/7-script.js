$(function () {
	let url = 'https://swapi.co/api/people/5/?format=json';
	$.get(url, function (data, textStatus) {
		var getName = data['getName'];
		$('#character').append(getName);
	});
});
