#!/usr/bin/node
const $ = window.$;
const redSelector = 'DIV#red_header';
$(redSelector).click(function () {
  $(redSelector).addClass('red');
});
