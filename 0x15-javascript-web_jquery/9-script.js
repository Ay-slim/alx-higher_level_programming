#!/usr/bin/node
const $ = window.$;
const helloUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(helloUrl, function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});
