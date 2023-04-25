#!/usr/bin/node
/* a script that reads a file and
 * prints its contents
 */
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
