#!/usr/bin/node
/**
 * a script that gets number of times an
 * actor appears in films
 */
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let num = 0;
    for (const i of results) {
      if (i.characters.find((character) => character.endsWith('/18/'))) {
        num++;
      }
    }
    console.log(num);
  }
});
