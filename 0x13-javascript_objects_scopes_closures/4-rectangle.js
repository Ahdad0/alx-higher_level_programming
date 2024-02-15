#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ss = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
	ss += 'X';
      }
      if (i + 1 < this.height) {
	ss += '\n';
      }
    }
    console.log(ss);
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    let copy = this.width;
    this.width = this.height;
    this.height = copy;
  }
};
