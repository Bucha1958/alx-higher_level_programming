#!/usr/bin/node
const process = require("process");
let args = process.argv;
let myVal = parseInt(args[2]);
if (args.length < 3)
{
	console.log("Not a number");
}
else
{
	if (myVal)
	{
		console.log("My number:" + myVal);
	}
	else
	{
		console.log("Not a number");
	}
}
