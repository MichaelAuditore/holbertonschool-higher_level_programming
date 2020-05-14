const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

fetch(URL)
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
    const div = $('#hello');
    div.html(myJson.hello);
  });
