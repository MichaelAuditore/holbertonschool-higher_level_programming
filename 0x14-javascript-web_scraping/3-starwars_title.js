#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the title of movie by ID passed as arg */
const REQUEST = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
REQUEST(URL, function (err, resp, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
