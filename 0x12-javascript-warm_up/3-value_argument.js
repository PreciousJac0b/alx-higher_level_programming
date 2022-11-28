#!/usr/bin/node

const numberOfArgs = process.argv;
if (numberOfArgs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(numberOfArgs[2]);
}
