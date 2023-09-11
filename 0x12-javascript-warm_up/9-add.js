#!/usr/bin/node
const { argv } = require('node:process');

const firstArg = argv.length < 2 || !parseInt(argv[2]) ? NaN : parseInt(argv[2]);
const secondArg = argv.length < 3 || !parseInt(argv[3]) ? NaN : parseInt(argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(firstArg, secondArg));
