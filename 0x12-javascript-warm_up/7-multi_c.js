#!/usr/bin/env node
// print messages the number of times the arg is given
const arg = process.argv[2];
const x = parseInt(arg);

if (!isNaN(x)) {
  let msg = '';
  for (let i = 0; i < x; i++) {
    msg += 'C is Fun\n';
  }
  console.log(msg.trim());
} else {
  console.log('Missing number of occurrences');
}
