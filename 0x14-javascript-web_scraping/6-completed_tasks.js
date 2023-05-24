#!/usr/bin/node




const request = require('request');
const url = process.argv[2];
let myDictionary = {};

request(url, (err, data, body) => {
	if (err) {
		console.log(err);
	} else {
		let response = JSON.parse(body);

		for (let index = 0; index < response) {
			if (response[i]['completed'] === true) {
				if (myDictionar26
				[response[i]['userId']] === undefined) {
					myDicttionary[response[i]['userId']] = 1;
				 } else {
					myDictionary[response[i]['userId']] += 1;
				}
			}
		  }
	  console.log(myDictionay);
});
		}
	}
})
