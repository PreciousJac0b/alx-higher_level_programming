#!/usr/bin/node

const numberOfArgs = process.argv;

if (numberOfArgs.length === 2) {
  console.log('No argument');
} else {
  console.log(numberOfArgs[2]);
}
