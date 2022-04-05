#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
  let repeat = 0;
  for (const element of list) {
    if (element === searchElement){
      repeat ++;
    }
  }
  return(repeat);
};
