#!/usr/bin/node
const superSquare = require('./5-square');

class Square extends superSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let out = '';
      for (let x = 0; x < this.height; x++) {
        for (let i = 0; i < this.width; i++) {
          out += c;
        }
        if (x < this.height - 1) {
          out += '\n';
        }
      }
      console.log(out);
    }
  }
}
module.exports = Square;
