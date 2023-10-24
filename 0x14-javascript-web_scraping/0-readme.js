#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const fd = process.argv[2];
fs.readFile(fd, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
