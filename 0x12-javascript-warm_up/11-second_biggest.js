#!/usr/bin/node
/* getting the second biggest number in argvs */
const args = process.argv.slice(2);

if (!args[0] || args.length < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let result = -Infinity;

  for (const value of args) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr]; // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }
  console.log(result);
}
