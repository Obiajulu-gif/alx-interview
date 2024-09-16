#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
 */
const request = require('request');

const movieID = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);

  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
