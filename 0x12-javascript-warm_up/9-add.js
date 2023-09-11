#!/usr/bin/node
const firstArg = process.argv.length < 2 || !parseInt(process.argv[2]) ? NaN : parseInt(process.argv[2]);
const secondArg = process.argv.length < 3 || !parseInt(process.argv[3]) ? NaN : parseInt(process.argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(firstArg, secondArg));
