#!/usr/bin/node

/* Prints out the status code of a particular request */

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(apiUrl, async function (error, response, body) {
  if (error) throw error;
  const characters = JSON.parse(body).characters;
  for (const elem of characters) {
    await new Promise((resolve, reject) => {
      request.get(elem, function (errors, responses, bodies) {
        if (errors) reject(errors);
        const result = JSON.parse(bodies).name;
        console.log(result);
        resolve();
      });
    });
  }
});
