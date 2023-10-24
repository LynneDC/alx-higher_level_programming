#!/usr/bin/node

const request = require('request');
const epsd_num = process.argv[2];
const api_url = 'https://swapi-api.alx-tools.com/api/films/';

request(api_url + epsd_num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
