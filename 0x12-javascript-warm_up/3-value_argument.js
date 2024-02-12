#!/usr/bin/node

const first = process.argv[2];

if (first === undefined) {
  console.log('No Argument');
} else {
  console.log(first);
}
