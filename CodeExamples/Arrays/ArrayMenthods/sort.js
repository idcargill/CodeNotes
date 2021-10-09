// Sort
// String values ascending by default
let arr = [1, 3, 5, 10, 100, 12, 22, 50];
let words = ["Ian", "angela", "Jae", "osborne"];

let sortStrings = arr.sort();
let sortNumAsc = arr.sort((a, b) => a - b);
let sortNumDesc = arr.sort((a, b) => b - a);

// Sorted by same case
let sortedCaps = words.sort((a, b) => {
  if (a.toUpperCase() < b.toUpperCase()) {
    return -1;
  }
  if (a.toUpperCase() > b.toUpperCase()) {
    return 1;
  } else {
    return 0;
  }
});

console.log(sortNumAsc);
console.log(sortNumDesc);
console.log(sortedCaps);
