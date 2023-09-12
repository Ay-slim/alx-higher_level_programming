#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let strPrt = '';
    for (let i = 0; i < this.width; i++) {
      strPrt += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(strPrt);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
