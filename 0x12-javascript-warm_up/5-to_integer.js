#!/usr/bin/node
const { argv } = require('node:process');

const num = argv.length > 2 && Boolean(parseInt(argv[2])) ? parseInt(argv[2]) : 'Not a number';
console.log(num);
