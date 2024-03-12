#!/usr/bin/node
let a = 0;
process.argv.forEach((val, index) => {
  a++;
  if (index === 2) {
    console.log(`${val}`);
  }
});
if (a <= 2) {
  console.log('No argument');
}
