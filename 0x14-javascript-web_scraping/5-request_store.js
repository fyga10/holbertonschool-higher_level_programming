#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filepath = process.argv[3];
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFileSync(filepath, response.body);
});
