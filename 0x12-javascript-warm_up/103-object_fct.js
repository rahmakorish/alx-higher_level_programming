#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function incr () {
  self.value++;
}
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
