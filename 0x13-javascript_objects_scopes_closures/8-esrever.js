#!/usr/bin/node

exports.esrever = function (list) {
  const nList = [];
  let n = list.length - 1;

  for (let i = 0; i < list.length; i++) {
    nList[i] = list[n];
    n -= 1;
  }

  return nList;
};
