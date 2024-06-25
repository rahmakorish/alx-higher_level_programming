#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rec = '';
    for (let i = 0; i < this.width; i++) {
      for (let x = 0; x < this.height; x++) {
        rec += 'X';
      }
      if (i < this.height - 1) {
        rec += '\n';
      }
    }
    console.log(rec);
  }
}
module.exports = Rectangle;
