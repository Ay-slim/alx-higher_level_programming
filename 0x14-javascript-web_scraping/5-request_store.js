#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const request = require('request');

const url = process.argv[2];
const fd = process.argv[3];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fd, body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
