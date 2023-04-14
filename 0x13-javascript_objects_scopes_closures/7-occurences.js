#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	
	let newArray = [];
	try {
		if (list.includes(searchElement) === true) {
			for (let i = 0; i < list.length; i++) {
				if (searchElement === list[i]) {
					newArray.push(searchElement);
				}
			}
		}
		return newArray.length;
	} catch (error) {
		return ("Error" + error);
	}
};


