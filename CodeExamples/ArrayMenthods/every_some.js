// EVERY
// checks every element in array for true/false
// returns true of false

const arr = [1, -5, 5, -15, 30];

function checkPositive(arr) {
  // return arr.every((i) => typeof i === "number");
  return arr.every((item) => item > 0);
}

console.log(checkPositive(arr));

//==========================================
// SOME
// Checks if any element in array is true
// returns true or false

// function checkPositive(arr) {
//   return arr.some((num) => num > 0);
// }

// let numbers = [1, 2, 3, -4, 5];

// let x = checkPositive(numbers);
// console.log(x);
