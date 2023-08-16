#!/usr/bin/node
const args = process.argv;
if ((args[2] && isNaN(Number(args[2]))) || args.length < 3) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(args[2]); i++) {
    let row = '';
    for (let j = 0; j < Number(args[2]); j++) {
      row += 'X ';
    }
    console.log(row);
  }
}
