#!/usr/bin/node
const firstArgs = process.argv[2];
const parsedArgs = parseInt(firstArgs, 10);

if (!Number.isNaN(parsedArgs)) {
  console.log(`My number: ${parsedArgs}`);
} else {
  console.log("Not a number");
}
