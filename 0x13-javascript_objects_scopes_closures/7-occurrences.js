#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let a = 0;

  for (let b = 0; b <= list.length; b++) {
    if (list[b] === searchElement) {
     a++;
    }
  }
  return a;
};
