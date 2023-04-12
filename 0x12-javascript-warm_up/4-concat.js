#!/usr/bin/node
const process = require("process");
let args = process.argv;
let firstName = args[2];
let secondName = args[3];
console.log(`${firstName} is ${secondName}`);

