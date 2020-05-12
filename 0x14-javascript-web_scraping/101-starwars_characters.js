#!/usr/bin/node
// print all character names of a SW movie got it by id
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let characters;
const dict = {};
request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  characters = JSON.parse(body).characters;
  for (const url of characters) {
    request(url, (error, response, body) =>
      !error && addNames(url, JSON.parse(body).name));
  }
});

function addNames (url, name) {
  dict[url] = name;
  if (Object.entries(dict).length === characters.length) {
    for (const url of characters) {
      console.log(dict[url]);
    }
  }
}
