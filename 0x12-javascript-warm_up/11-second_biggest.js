#!/usr/bin/node
const args = process.argv;
function secondLargest (arr) {
  if (!arr || arr.length < 3 || isNaN(Number(arr[3]))) {
    return 0;
  }
  const newArr = arr.slice(2);
  let firstLargest = -Infinity;
  let secondLargest = -Infinity;
  for (let i = 0; i < newArr.length; i++) {
    if (parseInt(newArr[i]) > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = parseInt(newArr[i]);
    }
  }
  return secondLargest;
}
console.log(secondLargest(args));
