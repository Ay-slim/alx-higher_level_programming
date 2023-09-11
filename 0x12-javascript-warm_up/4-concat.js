#!/usr/bin/node
const { argv } = require('node:process');

const firstArg = argv.length > 2 ? argv[2] : 'undefined';
const secondArg = argv.length > 3 ? argv[3] : 'undefined';
console.log(`${firstArg} is ${secondArg}`);
