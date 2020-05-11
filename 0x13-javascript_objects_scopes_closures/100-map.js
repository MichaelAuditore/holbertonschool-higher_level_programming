#!/usr/bin/node
/* Exports a list and generate new with the
   initial value multiplied by the index */
let list = require('./100-data').list;
console.log(list);
list = list.map(function (item, index) {
  return (item * index);
});
console.log(list);
