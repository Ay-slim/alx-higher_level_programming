#!/usr/bin/node
if (!tracker) {
  var tracker = 0;
}
exports.logMe = function (item) {
  console.log(`${tracker}: ${item}`);
  tracker++;
};
