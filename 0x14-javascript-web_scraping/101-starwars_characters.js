#!/usr/bin/node
/*
 * a script that prints starwars actors
 */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    for (const i of JSON.parse(body).characters) {
      request(i, function (error, response, body) {
        console.log(error || JSON.parse(body).name);
      });
    }
  }
});
