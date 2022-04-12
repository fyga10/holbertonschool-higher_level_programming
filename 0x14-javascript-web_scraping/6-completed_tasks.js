#!/usr/bin/node
const request = require('request');
request({ url: process.argv[2], json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const Task = {};
    for (const API of body) {
      if (API.completed === true) {
        if (Task[API.userId] === undefined) {
          Task[API.userId] = 0;
        }
        Task[API.userId] += 1;
      }
    }
    console.log(Task);
  }
});
