#!/usr/bin/node
const $ = window.$;
$(document).ready(
  function () {
    $('#btn_translate').click(function () {
      const inputVal = $('INPUT#language_code')[0].value;
      const helloUrl = `https://hellosalut.stefanbohacek.dev/?lang=${inputVal}`;
      $.get(helloUrl, function (data, textStatus) {
        $('DIV#hello').text(data.hello);
      });
    });
  }
);
