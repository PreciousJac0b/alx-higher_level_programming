#!/usr/bin/node

const arg = Math.floor(Number(process.argv[2]));

for (let i = 0; i < arg; i++) {
  for (let j = 0; j < arg; j++) {
    process.stdout.write('X');
  }
  console.log();
}
