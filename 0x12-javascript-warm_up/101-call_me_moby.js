#!/usr/bin/node
/* Function to call itself a number of times */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
