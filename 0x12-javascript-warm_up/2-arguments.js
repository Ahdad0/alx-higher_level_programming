#!/usr/bin/node

const { argv } = require('node:process');

const my = argv.length;

if (my === 2) {
  console.log('No argument');
} else if (my === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
