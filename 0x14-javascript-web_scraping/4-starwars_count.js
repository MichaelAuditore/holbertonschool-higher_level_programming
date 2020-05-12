#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the number of times a character with id 18 appears in movies */
const REQUEST = require('request');
REQUEST(process.argv[2], function (err, resp, body) {
  if (err) {
    console.error(err);
  }
  let times = 0;
  const MOVIES = JSON.parse(body).results;
  for (let i = 0; i < MOVIES.length; i++) {
    for (let j = 0; j < MOVIES[i].characters.length; j++) {
      if (MOVIES[i].characters[j].search('/18/') > 0) {
        times++;
      }
    }
  }
  console.log(times);
});
