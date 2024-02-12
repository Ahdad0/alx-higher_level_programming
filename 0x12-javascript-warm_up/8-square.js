#!/usr/bin/node

const first = process.argv[2];
const num = parseInt(first);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    console.log('XX');
  }
}
