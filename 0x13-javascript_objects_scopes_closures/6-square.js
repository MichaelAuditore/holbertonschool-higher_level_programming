#!/usr/bin/node
/* class Square inherits from Rectangle */
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  /* charPrint prints a square with a char passed to the function */
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
