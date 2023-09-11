#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 2 || !parseInt(argv[2])) {
  console.log('Missing size');
} else {
  let strVal = '';
  const size = parseInt(argv[2]);
  for (let i = 0; i < size; i++) {
    strVal += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(strVal);
  }
}
