#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the number of times a character with id 18 appears in movies */
const request = require('request');
const URL = process.argv[2];
request(URL, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body);
    let times = 0;
    for (const film of films.results) {
      for (const character of film.characters) {
        if (character.search('18') > 0) {
          times++;
        }
      }
    }
    console.log(times);
  }
});
