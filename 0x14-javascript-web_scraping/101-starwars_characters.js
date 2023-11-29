#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (!error) {
    for (let i = 0; i < body.characters.length; i++) {
      request(body.characters[i], { json: true }, (errorInside, responseInside, bodyInside) => {
        if (!errorInside) {
          console.log(bodyInside.name);
        } else {
          console.log(errorInside);
        }
      });
    }
  } else {
    console.log(error);
  }
});
