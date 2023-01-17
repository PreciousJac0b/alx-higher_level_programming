#!/usr/bin/node

/* Prints out the status code of a particular request */

const request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
