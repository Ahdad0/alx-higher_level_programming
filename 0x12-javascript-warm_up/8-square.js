#!/usr/bin/node

const first = process.argv[2];
const num = parseInt(first);
let list = '';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    for (let j = 0; j < first; j++) {
      list += 'X';
    }
    if (i + 1 < first) {
      list += '\n';
    } else {
      console.log(list);
    }
  }
}
