#!/usr/bin/node
const x = Number(process.argv[2]);
let sum = 1;
let f = x;
while (f > 1) {
  sum *= f;
  f--;
}
console.log(sum);
