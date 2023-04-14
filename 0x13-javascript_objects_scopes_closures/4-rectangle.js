#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	print () {
		for (let i = 0; i < this.height; i++) {
			let prt = '';
			for (let j = 0; j < this.weight; j++) {
				prt = prt + 'X';
			}
			console.log(prt);
		}
	}
	rotate () {
		let temp = this.height;
		this.height = this.width;
		this.width = temp;
	}
	double () {
		this.height = this.height *2;
		this.width = this.weight * 2; 
	}
}

module.exports = Rectangle;
