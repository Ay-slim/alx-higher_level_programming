#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
request(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res && res.statusCode}`);
  }
});
