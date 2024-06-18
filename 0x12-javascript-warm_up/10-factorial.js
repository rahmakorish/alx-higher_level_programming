#!/usr/bin/node
const inputy = Number(process.argv[2]);
function factorialnum (x) {
  let sum = 1;
  let f = x;
  if (f === 1) {
    sum = NaN;
  } else {
    while (f > 1) {
      sum *= f;
      f--;
    }
  }
  console.log(sum);
}
factorialnum(inputy);
