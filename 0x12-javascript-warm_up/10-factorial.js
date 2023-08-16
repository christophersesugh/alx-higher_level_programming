#!/usr/bin/node
const args = process.argv;
const arg = args[2];
function factorial (n) {
  if (isNaN(n) || !args || parseInt(n) <= 1) {
    return (1);
  }
  return parseInt(n) * factorial(parseInt(n) - 1);
}
console.log(factorial(arg));
