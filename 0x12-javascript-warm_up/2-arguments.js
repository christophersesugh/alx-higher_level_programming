#!/usr/bin/node
const args = process.argv;
if (args[2]) {
  console.log('Argument found');
} else if (args.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
