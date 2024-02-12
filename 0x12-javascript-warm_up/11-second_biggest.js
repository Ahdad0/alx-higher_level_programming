#!/usr/bin/node

function bigNum (l, index) {
  let num = l[0];

  for (let j = 1; j < index; j++) {
    if (num < l[j]) {
      num = l[j];
    }
  }

  return num;
}

let list = [];
let i;

for (i = 0; !(process.argv[i + 2] === undefined); i++) {
  list[i] = process.argv[i + 2];
}

if (list[0] === undefined || list[1] === undefined) {
  console.log(0);
} else {
  let number = bigNum(list, i);
  list = list.filter(item => item !== number);
  number = bigNum(list, i);
  console.log(number);
}
