#!/usr/bin/node

const { argv } = require('node:process');

const my = argv.length;

if (my === 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
