#!/usr/bin/node
/*
 * a script that gets the status code of a url
 */
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
});
