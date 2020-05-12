#!/usr/bin/node
/* Script to do a request to STAR WARS API
 and get the number of times a character with id 18 appears in movies */
const request = require('request');
const URL = process.argv[2];
request(URL, function (error, status, body) {
  if (error) {
    console.error(error);
  } else {
    const dict = {};
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      dict[tasks[i].userId] = 0;
    }
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        dict[tasks[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
