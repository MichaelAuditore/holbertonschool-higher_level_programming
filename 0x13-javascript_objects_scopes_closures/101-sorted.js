#!/usr/bin/node
/* Function to import a dictionary and print sort dictionary by user_id */
const dict = require('./101-data').dict;
const newDict = {};
let last = 0;
for (const [, value] of Object.entries(dict)) {
  const arr = [];
  for (const [key, value] of Object.entries(dict)) {
    if (last === value) {
      arr.push(key);
      newDict[value] = arr;
    }
  }
  last = value;
}
console.log(newDict);
