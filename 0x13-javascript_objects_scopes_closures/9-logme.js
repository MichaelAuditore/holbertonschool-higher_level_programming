#!/usr/bin/node
/* Function to reverse a list */
let myFuncCalls = 0;

exports.logMe = function (item) {
  console.log(myFuncCalls + ': ' + item);
  myFuncCalls++;
};
