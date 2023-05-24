#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.log(`Failed to retrieve movie: ${url}`);
      return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    let charactersCount = 0;

    function retrieveCharacter (characterUrl) {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log(`Failed to retrieve character: ${characterUrl}`);
          return;
        }

        const characterData = JSON.parse(body);
        const characterName = characterData.name;
        console.log(characterName);

        charactersCount++;
        if (charactersCount === characters.length) {
          return;
        }
        const nextCharacterUrl = characters[charactersCount];
        retrieveCharacter(nextCharacterUrl);
      });
    }
    retrieveCharacter(characters[0]);
  });
}

getMovieCharacters(movieId);
