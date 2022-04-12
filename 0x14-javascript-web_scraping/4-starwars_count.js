#!/usr/bin/node
const request = require('request');
const id = 18;

request({ url: process.argv[2], json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = body.results;
    let count = 0;
    for (const element of results) {
      for (const char of element.characters) {
        if (char.endsWith(id)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
