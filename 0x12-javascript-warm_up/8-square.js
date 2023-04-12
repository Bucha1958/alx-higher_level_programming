#!/usr/bin/node
const process = require('process');
let args = process.argv;
let i;
let j;
if (args.length < 3 || isNaN(parseInt(args[2])))
{
	console.log("Missing size");
}
else
{
	let myVal = parseInt(args[2]);
	i = 0;
	while (i < myVal)
	{
		prt = '';
		j = 0
		while (j < myVal) {
			prt = prt + 'X';
			j++;
		}
		console.log(prt);
		i++;
	}
}
