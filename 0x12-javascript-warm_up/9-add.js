#!/usr/bin/node
/* Adds to numbers */
const args = process.argv.slice(2);

function add (a, b) {
  a = parseInt(a, 10);
  b = parseInt(b, 10);
  console.log(a + b);
}

add(args[0], args[1]);
