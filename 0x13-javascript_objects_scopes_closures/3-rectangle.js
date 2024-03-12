#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
    this.width = w;
    this.height = h;
  }
  }
  print()
  {
        let out = '';
        for (let x = 0; x < this.height; x++)
        {
            for (let i = 0; i < this.width; i++)
            {
                out += 'X';
            }
                out += '\n';
            }
          console.log(out);
        }
        
    }
  module.exports = Rectangle;