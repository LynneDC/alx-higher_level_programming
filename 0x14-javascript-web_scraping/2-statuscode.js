#!/usr/bin/node

const request = require('fs');

request(process.argv[2], function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log('code', data && data.statusCode);
  }
});
