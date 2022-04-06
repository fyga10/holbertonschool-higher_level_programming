#!/usr/bin/node
const dict1 = require('./101-data').dict;
const dict2 = {};
for (const key in dict1) {
  if (!dict2[dict1[key]]) {
    dict2[dict1[key]] = [];
  }
  dict2[dict1[key]].push(key);
}
console.log(dict2);
