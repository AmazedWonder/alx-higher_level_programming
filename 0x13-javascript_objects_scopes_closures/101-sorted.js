#!/usr/bin/node
const { dict } = require('./101-data');

const result = {};

for (const userId in dict) {
  const noOccurrences = dict[userId];

  if (result[noOccurrences]) {
    result[noOccurrences].push(userId);
  } else {
    result[noOccurrences] = [userId];
  }
}

console.log(result);
