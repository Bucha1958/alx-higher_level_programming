#!/usr/bin/node

exports.esrever = function (list) {
	let newArray = [];
	for (let i = list.length; i > 0; i--) {
		newArray.push(list[i - 1]);
	}
	return (newArray);
}
