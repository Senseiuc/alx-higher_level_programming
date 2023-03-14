#!/usr/bin/node

const data = require('./100-data.js').list;
console.log(data);
const newList = data.map((x, index) => x * index);
console.log(newList);
