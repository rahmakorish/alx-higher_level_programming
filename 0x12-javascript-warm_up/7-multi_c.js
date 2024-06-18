#!/usr/bin/node
const i = process.argv[2];
let x = 0;
if (!Number(i)) {
  console.log('Missing number of occurrences');
} else {
  while (x < i) {
    console.log('C is fun');
    x++;
  }
}
