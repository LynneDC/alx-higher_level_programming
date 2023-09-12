#!/usr/bin/node
// define function and call it
exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
