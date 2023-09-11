#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  for (let j = 0; j < parseInt(x); j++) {
    theFunction();
  }
}
