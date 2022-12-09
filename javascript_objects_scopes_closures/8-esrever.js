#!/usr/bin/node
exports.esrever = function (list) {
  const mylist = [];
  for (let i = list.length; i > 0; i--) {
    mylist.push(list[i - 1]);
  }
  return mylist;
};
