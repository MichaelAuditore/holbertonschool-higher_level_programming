#!/usr/bin/node

/* Concat files script with JS */
const args = process.argv.slice(2);
var fs = require('fs');

const content = fs.readFileSync(args[0], 'utf-8');
const content2 = fs.readFileSync(args[1], 'utf-8');

fs.writeFileSync(args[2], (content + content2));
