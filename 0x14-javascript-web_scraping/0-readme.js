#!/usr/bin/node

/* Reads content in a file  */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(err || data);
});
