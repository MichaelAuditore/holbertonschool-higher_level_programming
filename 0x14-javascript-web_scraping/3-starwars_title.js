#!/usr/bin/node
/* Request for STAR WARS API */
const request = require('request');

const page = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(page, function (error, status, body) {
  if (status.statusCode == 200) {
    console.log(JSON.parse(body).title);
  } else if (error) {
    console.log(error);
  } else {
    console.log('The Force Awakens');
  }
});
