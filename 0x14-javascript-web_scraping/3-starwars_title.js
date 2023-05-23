#!/usr/bin/node
const movieId = process.argv[2];

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + movieId, (err, data, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
