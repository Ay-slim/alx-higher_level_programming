#!/usr/bin/node
const $ = window.$;
const togSelector = 'DIV#toggle_header';
$(togSelector).addClass('green');
$(togSelector).click(function () {
  if ($(togSelector).hasClass('green')) {
    $(togSelector).removeClass('green');
    $(togSelector).addClass('red');
  } else {
    $(togSelector).removeClass('red');
    $(togSelector).addClass('green');
  }
});
