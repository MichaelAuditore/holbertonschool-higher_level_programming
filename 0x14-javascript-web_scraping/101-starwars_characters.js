#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the characters  */
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(URL, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, status, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
