#!/usr/bin/node
const $ = window.$;
const titleUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(titleUrl, function (data, textStatus) {
  for (const j of data.results) {
    $('UL#list_movies').append(`<li>${j.title}</li>`);
  }
});
