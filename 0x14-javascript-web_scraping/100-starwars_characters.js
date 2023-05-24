#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    characters.forEach(characterUrl => {
      request(characterUrl, (err, response, body) => {
        if (err) {
          console.log(`Failed to retrieve character: ${characterUrl}`);
          return;
        }
        const characterData = JSON.parse(body);
        const characterName = characterData.name;
        console.log(characterName);
      });
    });
  });
}

getMovieCharacters(movieId);
