#!/usr/bin/node
/* class Square inherits from Rectangle */
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
