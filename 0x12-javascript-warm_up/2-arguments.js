#!/usr/bin/node

// handles arguments bassed on command line
const argCount = process.argv.length - 2;
if (argCount === 0) {
  console.log('No argument');
} else if (argCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
