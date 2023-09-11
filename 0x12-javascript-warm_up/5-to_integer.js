#!/usr/bin/node
const num = process.argv.length > 2 && Boolean(parseInt(process.argv[2])) ? parseInt(process.argv[2]) : 'Not a number';
console.log(num);
