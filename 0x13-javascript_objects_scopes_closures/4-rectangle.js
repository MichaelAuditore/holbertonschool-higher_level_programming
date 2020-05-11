#!/usr/bin/node
/* Class Rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /* Function print - draws a rectangle */
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  /* Function double - multiplies the width and the height by 2 */
  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }

  /* Function rotate - exchanges the width and the height of the rectangle */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};
