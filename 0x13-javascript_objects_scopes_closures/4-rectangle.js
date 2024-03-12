#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let out = '';
    for (let x = 0; x < this.height; x++) {
      for (let i = 0; i < this.width; i++) {
        out += 'X';
      }
      if (x < this.height - 1) {
        out += '\n';
      }
    }
    console.log(out);
  }

  rotate () {
    const heighty = this.height;
    this.height = this.width;
    this.width = heighty;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
