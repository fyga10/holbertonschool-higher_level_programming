#!/usr/bin/node
const request = require('request');
const url_id = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url_id, function(err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
