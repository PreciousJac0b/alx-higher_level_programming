#!/usr/bin/node

/* Prints out the status code of a particular request */

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) throw error;
  const results = JSON.parse(body);
  const numOfTasks = {};
  for (const elem of results) {
    if (elem.completed) {
      if (!numOfTasks[elem.userId]) {
        numOfTasks[elem.userId] = 1;
      } else {
        numOfTasks[elem.userId] += 1;
      }
    }
  }
  console.log(numOfTasks);
});
