#!/usr/bin/node
/*
 * a script that prints starwars title
 */
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
