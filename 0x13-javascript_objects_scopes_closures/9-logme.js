#!/usr/bin/node
const itemsList = [];
exports.logMe = function (item) {
  console.log(`${itemsList.length}: ${item}`);
  itemsList.push(item);
};
