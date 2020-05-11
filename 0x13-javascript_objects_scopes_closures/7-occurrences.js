#!/usr/bin/node
/* Function to return number of ocurrences of a element in a list */
exports.nbOccurences = function (list, searchElement) {
  if (list && searchElement) {
    let n = 0;
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        n++;
      }
    }
    return (n);
  }
  return (0);
};
