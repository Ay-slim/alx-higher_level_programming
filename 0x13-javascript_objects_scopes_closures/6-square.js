#!/usr/bin/node
const SquareOld = require('./5-square');
module.exports = class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const strCmp = c ?? 'X';
    let strPrt = '';
    for (let i = 0; i < this.width; i++) {
      strPrt += strCmp;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(strPrt);
    }
  }
};
