#!/usr/bin/node
/* Converts a string parameter into a numebr */
const args = process.argv.slice(2);
const number = parseInt(args[0], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
