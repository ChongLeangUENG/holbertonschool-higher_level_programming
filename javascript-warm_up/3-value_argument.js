#!/usr/bin/node

const args = process.argv;
let index = 0;
while (index in args) {
  index++;
}
if (index === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
