#!/usr/bin/node
const list = require('./100-data').list;
const nlist = list.map((item, index, list) => item * index);
console.log(list);
console.log(nlist);
