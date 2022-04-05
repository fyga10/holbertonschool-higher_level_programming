#!/usr/bin/node
const Square = require('./5-square');
class Square1 extends Square {
    charPrint (c) {
      if (c) {
        for (let i = 0; i < this.height; i++) {
          console.log('c'.repeat(this.width));
        }
      } else {
          return super.print(c);
        }
      }
    }
module.exports = Square1;
