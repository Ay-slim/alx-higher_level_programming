#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const fd = process.argv[2];
const txt = process.argv[3];
fs.writeFile(fd, txt, (err) => {
  if (err) {
    console.log(err);
  }
});
