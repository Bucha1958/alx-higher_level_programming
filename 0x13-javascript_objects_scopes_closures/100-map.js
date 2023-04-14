#!/usr/bin/node
let firstList = require("./100-data.js").list;
let i = 0;
let secondList = firstList.map((x) => x * i++);
console.log(firstList);
console.log(secondList);
