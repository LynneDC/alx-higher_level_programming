#!/usr/bin/node
// prints the second biggest int of the given array
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const scnd = arr.sort(function (a, b) { return b - a; })[1];
  console.log(scnd);
}
