#!/usr/bin/node
const callMeMoby = (a, func) => {
  for (let j = 0; j < parseInt(a); j++) {
    func();
  }
}
exports.callMeMoby = callMeMoby;
