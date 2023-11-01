#!/usr/bin/node
const $ = window.$;
const redSelector = 'DIV#red_header';
$(redSelector).click(function () {
  $(redSelector).css('color', '#FF0000');
});
