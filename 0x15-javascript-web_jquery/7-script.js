#!/usr/bin/node
const $ = window.$;
const nameUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(nameUrl, function (data, textStatus) {
  $('DIV#character').text(data.name);
});
