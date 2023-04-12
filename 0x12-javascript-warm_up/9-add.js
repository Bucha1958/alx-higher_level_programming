#!/usr/bin/node
const process = require('process');
let args = process.argv;
function add(a, b) {
	let total = parseInt(a) + parseInt(b);
	console.log(total);
}
add(args[2], args[3]);
