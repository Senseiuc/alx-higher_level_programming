#!/usr/bin/node
const request = require('request');
const endPoint = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(endPoint, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const myList = [];
    characters.forEach(character => {
      myList.push(new Promise((resolve, reject) => {
        request.get(character, function (err, response, body) {
          if (err) {
            reject(err);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(myList).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
