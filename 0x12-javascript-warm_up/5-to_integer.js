#!/usr/bin/node
const Var = process.argv[2];
if (isNaN(Var) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Var);
}
