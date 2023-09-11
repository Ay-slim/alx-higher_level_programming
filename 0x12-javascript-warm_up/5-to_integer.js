#!/usr/bin/node
console.log(process.argv.length > 2 && parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
