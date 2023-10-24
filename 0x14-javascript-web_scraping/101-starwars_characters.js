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
const printNames = (charIds, charMap) => {
  charIds.forEach(id => {
    console.log(charMap[id]);
  });
};
const charMap = {};
request(fUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedJson = JSON.parse(body);
    const charIds = parsedJson.characters.map(idExtractor);
    for (const j in charIds) {
      request(`${pUrl}${charIds[j]}/`, (err, res, pBody) => {
        if (err) {
          console.log(err);
        }
        const parsedPerson = JSON.parse(pBody);
        charMap[charIds[j]] = parsedPerson.name;
        if (parseInt(j) === charIds.length - 1) {
          setTimeout(() => printNames(charIds, charMap), 2000);
        }
      });
    }
  }
});
