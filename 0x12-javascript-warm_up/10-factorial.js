#!/usr/bin/node
function fact (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return (fact(a - 1) * a);
  }
}
console.log(`${fact(Number(process.argv[2]))}`);
