// Currying

// function unCurried(x, y) {
//   return x + y;
// }

// // function curried(x) {
// //   return function (y) {
// //     return x + y;
// //   };
// // }

// const curried = (x) => (y) => x + y;

// let x = curried(1)(2);
// console.log(x);
// // curried(1)(2) would return 3.

// Curried Function  // Higher order Functions.
// Takes a function as argument
// Each argument is converted to a chain of functions
// Function that returns a function that takes a function...

// function add(x) {
//   return function (y) {
//     return function (z) {
//       return x + y + z;
//     };
//   };
// }

// Example
// function add(x) {
//   return (y) => (z) => x + y + z;
// }

// let x = add(10)(20)(30);
// console.log(x);
///===============

// Example
// function sumAll(arr) {
//   let large = Math.max(...arr);
//   let small = Math.min(...arr);

//   return small !== large ? small + sumAll([small + 1, large]) : small;

// SAME as Ternery
// if (small !== large ) {
//   return small + sumAll([small + 1, large])
// } else {
//   return small;
// }
// }

// let x = sumAll([4, 1]);
// console.log(x);
// ================

// EXAMPLE
// DIFF from 2 Arrays
// function diffArray(arr1, arr2) {
//   const notInArr2 = arr1.filter((item) => !arr2.includes(item));
//   const notInArr1 = arr2.filter((item) => !arr1.includes(item));
//   return [...notInArr1, ...notInArr2];
// }

// Example, same concept as above but shorter with chaining.
// function diffArray(arr1, arr2) {
//   return arr1
//     .concat(arr2)
//     .filter(item => !arr1.includes(item) || !arr2.includes(item));
// }

// let x = diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
// let y = diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4]); // ['piglet', 4]

// console.log(x);
// console.log(y);
// =====================

// EXAMPLE
// function destroyer(arr) {
//   const params = Array.from(arguments).slice(1, arguments.length);
//   return arr.filter((item) => !params.includes(item));
// }

// let x = destroyer([1, 2, 3, 1, 2, 3], 2, 3);
// console.log(x);
// ==================

function whatIsInAName(collection, source) {
  const srcKey = Object.keys(source);

  return collection.filter((obj) => {
    return srcKey.every((key) => {
      return obj.hasOwnProperty(key) && obj[key] === source[key];
    });
  });
}

let x = whatIsInAName(
  [
    { first: "Romeo", last: "Montague" },
    { first: "Mercutio", last: null },
    { first: "Tybalt", last: "Capulet" },
  ],
  { last: "Capulet" }
);

console.log(x);
