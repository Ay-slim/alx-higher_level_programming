#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = {};
for (const i in dict) {
  sortedDict[dict[i]] = sortedDict[dict[i]] && sortedDict[dict[i]].length ? sortedDict[dict[i]].concat([i]) : [i];
}
console.log(sortedDict);
