#!/usr/bin/node
const process = require("process");
let args = process.argv;
let convert = parseInt(args[2]);
let i;
if (args.length < 3) {
	console.log("Missing number of occurrences");
} else {
	if (convert) {
		for (i = 0; i < convert; i++) {
			console.log("C is fun");
		}		
	}
}
