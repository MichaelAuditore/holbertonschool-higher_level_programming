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
    for (const task of tasks) {
      if (task.completed) {
        if (dict[task.userId]) {
          dict[task.userId] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
