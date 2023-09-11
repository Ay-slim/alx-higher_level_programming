#!/usr/bin/node
const firstArg = process.argv.length < 2 || !parseInt(process.argv[2]) || parseInt(process.argv[2]) < 0 ? NaN : parseInt(process.argv[2]);
function factorial (a) {
  if (!a) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(firstArg));
