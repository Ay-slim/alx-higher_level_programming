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
    request(pUrl, (err, res, pBody) => {
      if (err) {
        console.log(err);
      }
      const parsedPeople = JSON.parse(pBody);
      parsedPeople.results.forEach(person => {
        if (charIds.includes(idExtractor(person.url))) {
          console.log(person.name);
        }
      });
    });
  }
});
