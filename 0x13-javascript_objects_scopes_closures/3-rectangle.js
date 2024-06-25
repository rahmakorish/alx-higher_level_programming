#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
    print(){
        for(let i = 0; i < w; i++)
            {
                for(let x = 0; x < h; x++)
                    console.log('#');
            }
    }
  }
  module.exports = Rectangle;
  