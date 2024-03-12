#!/usr/bin/node
const Var = process.argv[2];
if (isNaN(Var) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < Var; a++) {
    console.log('C is fun');
  }
}
