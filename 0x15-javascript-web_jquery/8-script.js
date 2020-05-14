const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(URL)
    .then(function (response) {
        return response.json();
    })
    .then(function (myJson) {
        let list = $('#list_movies');
        for (title of myJson.results) {
            list.append('<li>' + title.title + '</li>');
        }
    });