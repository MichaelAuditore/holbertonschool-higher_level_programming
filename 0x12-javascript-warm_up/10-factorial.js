#!/usr/bin/node
/* Recursive factorial function */
const args = process.argv.slice(2);

function factorial (number) {
  if (number <= 0 || isNaN(number)) {
    return 1;
  }
  return (number * factorial(number - 1));
}
console.log(factorial(parseInt(args[0])));
