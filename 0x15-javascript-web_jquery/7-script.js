const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(URL)
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
    const character = $('#character');
    character.html(myJson.name);
  });
