#!/usr/bin/node

const baseSquare = require("./5-square.js");

class Square extends baseSquare{
    constructor (size) {
	super(size, size);
    }

    charPrint (c) {
	let alphabet;
	if (c === undefined) {
	    alphabet = 'X';
	} else {
	    alphabet = c;
	}

	for (let i = 0; i < this.height; i++) {
	    let ptr = '';
	    for (let j = 0; j < this.width; j++) {
		ptr = ptr + alphabet;
	    }
	    console.log(ptr);
	}
    }
}

module.exports = Square;
