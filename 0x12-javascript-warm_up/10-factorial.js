#!/usr/bin/node
const process = require("process");
let args = process.argv;

function factorial(x) {
	
	if (x === 0 || isNaN(parseInt(x))) {
		return (1);
	} else {
		return (x * factorial(x - 1));
	}
}
console.log(factorial(args[2]));

