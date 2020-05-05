#!/usr/bin/node
/* Print an square given a size */
const args = process.argv.slice(2);
if (!args[0] || isNaN(parseInt(args[0], 10))) {
  console.log('Missing size');
} else {
  const len = parseInt(args[0], 10);
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
