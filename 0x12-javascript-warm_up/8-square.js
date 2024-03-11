#!/usr/bin/node
const i = process.argv[2];
let x = 0;
let j = 0;
if (!Number(i)) {
  console.log('Missing size');
} else {
  while (j < i) {
    while (x < i) {
      console.log('X');
      x++;
    }
    j++;
  }
}
