#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const args = [];
  for (let j = 2; j < argv.length; j++) {
    if (!args.includes(argv[j])) {
      args.push(argv[j]);
    }
  }
  const sortedArgs = args.sort((a, b) => a - b);
  console.log(sortedArgs[sortedArgs.length - 2]);
}
