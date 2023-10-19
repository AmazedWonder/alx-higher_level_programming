#!/usr/bin/node
const fs = require('fs');

const firArg = fs.readFileSync(process.argv[2]).toString();
const secArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firArg + secArg);
