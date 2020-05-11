#!/usr/bin/node
/* Function to import a dictionary and print sort dictionary by user_id */
const dict = require('./101-data').dict;
const listValues = new Set(Object.values(dict));
const result = {};
/* fill the dictionary with empty list for each key */
listValues.forEach(element => {
  result[element] = [];
});
for (const key1 of Object.keys(result)) {
  for (const key2 of Object.keys(dict)) {
    if (dict[key2] === parseInt(key1)) {
      result[key1].push(key2);
    }
  }
}
console.log(result);
