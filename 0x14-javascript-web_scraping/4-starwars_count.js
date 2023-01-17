#!/usr/bin/node

/* Prints out the status code of a particular request */

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) throw error;
  let counter = 0;
  const results = JSON.parse(body).results;
  for (const elem of results) {
    const characters = elem.characters;
    for (const elems of characters) {
      if (elems.includes('/18/')) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
