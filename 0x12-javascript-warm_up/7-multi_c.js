#!/usr/bin/node
let n = 0;
if (isNaN(process.argv[2]) === false) {
  const num = process.argv[2];
  while (n < num) {
    console.log('C is fun');
    n++;
  }
} else {
  console.log('Missing number of occurrences');
}
