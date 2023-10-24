#!/usr/bin/node
const process = require('process');
const request = require('request');

const movieId = process.argv[2];
const fUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
const pUrl = 'https://swapi-api.alx-tools.com/api/people/';
const idExtractor = (char) => {
  const charSplit = char.split('/');
  return charSplit[charSplit.length - 2];
};
request(fUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedJson = JSON.parse(body);
    const charIds = parsedJson.characters.map(idExtractor);
    for (const j of charIds) {
      request(`${pUrl}${j}/`, (err, res, pBody) => {
        if (err) {
          console.log(err);
        }
        const parsedPerson = JSON.parse(pBody);
        console.log(parsedPerson.name);
      });
    }
  }
}
);
