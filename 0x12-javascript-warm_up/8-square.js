#!/usr/bin/node
const i = process.argv[2];
let x = 0;
let j = 0;
let out = '';
let total = '';
if (!Number(i)) {
  console.log('Missing size');
} else {
  while (j < i) {
    while (x < i) {
      out += 'X';
      x++;
    }
    total += out;
    j++;
    if (j !== i) {
      total += '\n';
    } else {
      continue;
    }
  }
}
console.log(total);
