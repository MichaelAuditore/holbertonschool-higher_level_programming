#!/usr/bin/node
/* Script that writes what will be the content of a file. Passed by args */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.error(err);
  }
});
