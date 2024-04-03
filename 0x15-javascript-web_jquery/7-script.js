$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function ({ name }, status) {
  if (status === 'success') {
    $('DIV#character').text(name);
  }
});
