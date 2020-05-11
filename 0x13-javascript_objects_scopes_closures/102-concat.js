#!/usr/bin/env node

/* Concat files script with JS */
const args = process.argv.slice(2);
var path = require('path');
var fs = require('fs');

const path1 = path.resolve(args[0]);
const path2 = path.resolve(args[1]);
const destination = path.resolve(args[2]);

const content = fs.readFileSync(path1);
const content2 = fs.readFileSync(path2);

fs.writeFileSync(destination, content + content2);
