#!/usr/bin/node

const first = process.argv[2];
const num = parseInt(first);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}