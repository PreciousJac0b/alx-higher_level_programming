#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  console.log(a + b);
}
if (!args[2] || !args[3]) {
  console.log('NaN');
}
add(Math.floor(Number(args[2])), Math.floor(Number(args[3])));
