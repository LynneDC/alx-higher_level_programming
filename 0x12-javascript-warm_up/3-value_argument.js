#!/usr/bin/node

// handles arguments bassed on command line
const argCount = process.argv[2];
if (argCount === undefined) {
  console.log('No argument');
} else {
  console.log(argCount);
}
