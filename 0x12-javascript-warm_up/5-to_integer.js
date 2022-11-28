#!/usr/bin/node

const argv = process.argv;
if (Number.isInteger(argv[2])) {
  console.log('Not a number');
} else {
  const n = Math.floor(Number(argv[2]));
  console.log(`My number: ${n}`);
}
