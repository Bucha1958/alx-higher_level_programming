#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const myDictionary = {};

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);

    for (let index = 0; index < response.length; index++) {
      if (response[index].completed === true) {
        if (myDictionary[response[index].userId] === undefined) {
          myDictionary[response[index].userId] = 1;
        } else {
          myDictionary[response[index].userId] += 1;
        }
      }
    }
  }
  console.log(myDictionary);
});
