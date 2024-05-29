const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (let a = 0; a <= data.results.length; a++) {
    $('UL#list_movies').append('<la>' + data.results[a].title + '</la>');
  }
});
