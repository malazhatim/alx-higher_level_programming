#!/usr/bin/node
const list = require('./100-data').list;
let a = 0;
const b = list.map(x => x * a++);
console.log(list);
console.log(b);
