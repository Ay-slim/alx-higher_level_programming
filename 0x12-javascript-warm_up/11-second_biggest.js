#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = [];
  for (let j = 2; j < process.argv.length; j++) {
    if (!args.includes(process.argv[j])) {
      args.push(process.argv[j]);
    }
  }
  const sortedArgs = args.sort((a, b) => a - b);
  console.log(sortedArgs[sortedArgs.length - 2]);
}
