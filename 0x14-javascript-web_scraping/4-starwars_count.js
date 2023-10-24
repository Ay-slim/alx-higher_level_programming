#!/usr/bin/node
const process = require('process');
const request = require('request');

const filmUrl = process.argv[2];
const targetId = 18;
const charLink = `https://swapi-api.alx-tools.com/api/people/${targetId}/`;
request(filmUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedJson = JSON.parse(body);
    const filmArr = parsedJson.results;
    const filmsWithWedgie = filmArr.filter(
      film => film.characters.includes(charLink)
    );
    console.log(filmsWithWedgie.length);
  }
});
