#!/usr/bin/node
const callMeMoby = (x, theFunction) => {
  for (let j = 0; j < parseInt(x); j++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
