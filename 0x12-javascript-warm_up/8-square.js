#!/usr/bin/node
const Var = process.argv[2];
let a = '';
if (isNaN(Var) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Var; i++) {
    a += 'X';
  }
  for (let i = 0; i < Var; i++) {
    console.log(a);
  }
}
