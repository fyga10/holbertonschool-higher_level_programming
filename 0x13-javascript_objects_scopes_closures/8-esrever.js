#!/usr/bin/node
exports.esrever = function (list) {
  const le = list.length - 1;
  const revers = [];
  for (let i = le; i >= 0; i--) {
    revers.push(list[i]);
  }
  return revers;
};
