#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const j of list) {
    if (j === searchElement) {
      count++;
    }
  }
  return count;
};
