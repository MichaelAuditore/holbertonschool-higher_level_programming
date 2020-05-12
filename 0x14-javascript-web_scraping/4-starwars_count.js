#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the number of times a character with id 18 appears in movies */
const request = require('request');
let times = 0;
const URL = process.argv[2];
const expected = 'https://swapi-api.hbtn.io/api/films';
if (URL === expected) {
  request(URL, function (error, status, body) {
    if (error) {
      console.error(error);
    }
    const lista = JSON.parse(body);
    for (let i = 0; i < lista.results.length; i++) {
      for (let j = 0; j < lista.results[i].characters.length; j++) {
        if (lista.results[i].characters[j].search('/18/') > 0) {
          times += 1;
        }
      }
    }
    console.log(times);
  });
}
