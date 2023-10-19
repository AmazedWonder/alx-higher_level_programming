#!/usr/bin/node
let noargs = 0;

exports.logMe = function (item) {
  console.log(noargs + ': ' + item);
  noargs++;
};
