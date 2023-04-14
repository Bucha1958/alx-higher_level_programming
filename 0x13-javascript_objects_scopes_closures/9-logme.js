#!/usr/bin/node
let list = [];
exports.logMe = function (item) {
	console.log(`${list.length}: ${item}`)
	list.push(item);
}
