#!/usr/bin/node
const $ = window.$;
const fetchAndDisplay = () => {
  const inputVal = $('INPUT#language_code')[0].value;
  const helloUrl = `https://hellosalut.stefanbohacek.dev/?lang=${inputVal}`;
  $.get(helloUrl, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
};
$(document).ready(
  function () {
    $('#btn_translate').click(function () {
      fetchAndDisplay();
    });
    $('INPUT#language_code').keypress(
      function (event) {
        if (event.which === 13) { fetchAndDisplay(); }
      }
    );
  }
);
