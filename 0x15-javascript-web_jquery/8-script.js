$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function ({ results }, status) {
  if (status === 'success') {
    results.forEach(function ({ title }) {
      $('UL#list_movies').append($('<li></li>').text(title));
    });
  }
});
