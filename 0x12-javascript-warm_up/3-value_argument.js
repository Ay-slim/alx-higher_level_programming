#!/usr/bin/node
const { argv } = require('node:process');

const firstArg = argv[2] ?? null;
if (!firstArg) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
