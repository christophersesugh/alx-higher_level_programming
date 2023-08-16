#!/usr/bin/node
const args = process.argv;
const farg = args[2]; const sarg = args[3];
function add (a, b) {
  if (!a || !b || isNaN(Number(a) || Number(b))) {
    return (NaN);
  }
  return (Number(a) + Number(b));
}
console.log(add(farg, sarg));
