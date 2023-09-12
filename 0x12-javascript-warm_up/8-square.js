#!/usr/bin/node
// print messages the number of times the arg is given

if (process.argv.length > 2) {
  const y = parseInt(process.argv[2]);
  if (isNaN(y) || y <= 0) {
    console.error('Invalid size');
  } else {
    for (let i = 0; i < y; i++) {
      let row = '';
      for (let j = 0; j < y; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.error('Missing size');
}
