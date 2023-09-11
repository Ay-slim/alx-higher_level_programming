#!/usr/bin/node
const { argv } = require('node:process');
console.log(argv.length < 3 ? 'No argument' : argv.length === 3 ? 'Argument found' : 'Arguments found');
