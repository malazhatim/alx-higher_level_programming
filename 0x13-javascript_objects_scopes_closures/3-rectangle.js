#!/usr/bin/node
module.exports = class Rectangle {
  constructor (a, b) {
    if (a > 0 && b > 0) {
      [this.width, this.height] = [a, b];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
