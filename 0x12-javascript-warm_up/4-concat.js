#!/usr/bin/node
/* Print two arguments in a same line */
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
