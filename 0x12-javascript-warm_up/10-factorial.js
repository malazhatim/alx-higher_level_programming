#!/usr/bin/node

function factorialize (Var) {
  let R = 1;
  for (let a = 1; a <= Var; a++) {
    R *= a;
  }
  return (R);
}
console.log(factorialize(parseInt(process.argv[2])));
