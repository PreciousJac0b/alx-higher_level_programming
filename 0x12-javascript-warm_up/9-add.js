#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return a + b;
}

console.log(add(Math.floor(Number(args[2])), Math.floor(Number(args[3]))));
