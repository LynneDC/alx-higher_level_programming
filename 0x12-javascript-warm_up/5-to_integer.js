#!/usr/bin/node

// Get the first command-line argument
// Check if the arg can be converted to an int using the unary+
const arg = process.argv[2];
const num = +arg;
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
