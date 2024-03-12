#!/usr/bin/node
function Biggest (arry) {
  let x = 0; let result = 0;

  for (const value of arry) {
    const a = Number(value);

    if (a > x) {
      [result, x] = [x, a];
    } else if (a < x && a > result) {
      result = a;
    }
  }

  return result;
}

console.log(Biggest(process.argv));
