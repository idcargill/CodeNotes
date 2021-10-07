/* 
forEach() - iterate   
map() - returns an equal array  
find() - returns the first element that matches
filter() - returns array of truth
sort() -  MUTATES Array

*/

// map  array.map() 9.23
// Reurns equal length array

const movies = [
  { title: "Fatman", rating: "Good" },
  { title: "Nightmare Before Christmas", rating: "Good" },
  { title: "Black Christmas", rating: "Good" },
  { title: "Bad Sandta", rating: "bad" },
  { title: "Die Hard", rating: "wtf" },
];

let goodMovies = movies.map((movie, idx) => {
  return movie.rating == "Good" ? movie.title : "Its Bad";
});

// console.log(goodMovies);

const num = [1, 2, 3, 4, 5];

let addNums = num.map((n) => {
  return n + 2;
});

// one line  =======================
let addNum2 = num.map((n) => n + 3);

// console.log('\t \t', addNum2);

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
