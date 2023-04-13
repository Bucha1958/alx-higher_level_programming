#!/usr/bin/node
const process = require("process");
let args = process.argv;

function secondHighest (arr) {
	if (arr.length <= 2 || arr.length === 3) {
		return (0);
	} else if (arr.length > 3) {
		let myArray = [];
		for (let i = 2; i < arr.length; i++) {
			myArray.push(parseInt(arr[i]));
		}
		let maxIndex = myArray.indexOf(Math.max.apply(null, myArray));
		let replaceMax = myArray.splice(maxIndex, 1, 0);
		let max = Math.max.apply(null, myArray);
		return (max);
	}	
}

let result = secondHighest(args);
console.log(result);
