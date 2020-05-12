#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the number of times a character with id 18 appears in movies */
const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
request(URL, function (error, status, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
