#!/usr/bin/node
/* Print "C is fun" given a number of times */
const args = process.argv.slice(2);
if (!args[0]) {
  console.log('Missing number of occurrences');
} else {
  const len = parseInt(args[0], 10);
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
}
