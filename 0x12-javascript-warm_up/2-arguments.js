#!/usr/bin/node

const my = process.argv.length;

if (my === 2) {
  console.log('No argument');
} else if (my === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
