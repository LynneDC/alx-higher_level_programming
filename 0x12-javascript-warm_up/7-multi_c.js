#!/usr/bin/node
// print messages the number of times the arg is given
const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is Fun');
  }
}
