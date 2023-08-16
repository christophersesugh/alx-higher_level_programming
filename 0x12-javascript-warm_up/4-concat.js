#!/usr/bin/node
const args = process.argv;
const fa = args[2];
const ta = args[3];
if (args[2] && args[3]) {
  console.log(fa + ' is ' + ta);
} else if (args[2]) {
  console.log(fa + ' is ' + undefined);
} else {
  console.log(undefined + ' is ' + undefined);
}
