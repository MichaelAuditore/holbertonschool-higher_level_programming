#!/usr/bin/node
/* Function to reverse a list */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
