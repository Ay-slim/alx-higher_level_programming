#!/usr/bin/node
const $ = window.$;
const redSelector = '#red_header';
$(redSelector).click(function () {
  $(redSelector).addClass('red');
});
