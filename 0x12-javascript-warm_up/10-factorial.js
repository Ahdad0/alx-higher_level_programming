#!/usr/bin/node

function facto (a) {
  if (a === 0) {
    return 1;
  } else {
    return facto(a - 1) * a;
  }
}

const first = process.argv[2];
const num = parseInt(first);

if (isNaN(num)) {
  console.log(1);
} else {
  const res = facto(num);
  console.log(res);
}
