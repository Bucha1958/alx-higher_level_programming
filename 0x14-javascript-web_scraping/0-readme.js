#!/usr/bin/node
let filePath = process.argv[2];

let fs = require('fs');

fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.log(err);
	} else {
		console.log(data.toString());
	}
});
