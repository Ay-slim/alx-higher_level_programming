#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
}
