#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const comp = {};
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedJson = JSON.parse(body);
    parsedJson.forEach(todo => {
      const strId = String(todo.userId);
      if (todo.completed) {
        if (!comp[strId]) {
          comp[strId] = 1;
        } else {
          comp[strId]++;
        }
      }
    });
    console.log(comp);
  }
});
