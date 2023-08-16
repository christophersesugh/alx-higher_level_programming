#!/usr/bin/node
const args = process.argv;
if (args.length === 3 && !isNaN(Number(args[2]))) {
  console.log('My number:', parseInt(args[2]));
} else {
  console.log('Not a number');
}
