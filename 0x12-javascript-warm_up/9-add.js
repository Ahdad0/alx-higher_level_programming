#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const first = process.argv[2];
const seconde = process.argv[3];

if (first === undefined || seconde === undefined) {
  console.log('NaN');
} else {
  const res = add(parseInt(first), parseInt(seconde));
  console.log(res);
}
