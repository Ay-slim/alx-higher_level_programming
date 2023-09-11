#!/usr/bin/node
const { argv } = require('node:process');

const firstArg = argv.length < 2 || !parseInt(argv[2]) || parseInt(argv[2]) < 0 ? NaN : parseInt(argv[2]);
function factorial (a) {
  if (!a) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(firstArg));
