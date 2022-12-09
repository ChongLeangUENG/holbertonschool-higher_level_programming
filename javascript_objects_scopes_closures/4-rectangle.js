#!/usr/bin/node

class Rectangle {
  // Class methods
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instant method print
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // Instant method rotate
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Instant method double
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
