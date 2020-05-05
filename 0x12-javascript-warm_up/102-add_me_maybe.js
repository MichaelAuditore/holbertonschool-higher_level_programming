#!/usr/bin/node
/* Function to call itself a number of times */
exports.addMeMaybe = function (x, theFunction) {
  theFunction(x + 1);
};
