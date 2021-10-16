// REGEX

// regex.text(str)       T/F
// string.match(regex);  string  returns array

// Replace in String
// let str = "The fish is super hot";

// let newStr = str.replace(/[T]/, "The Cat");
// console.log(newStr);

//

// // 5
// const isCapitalized = (str) => {
//   return str.match(/[A-Z]{1}[a-z]+/g);
// };

// let longString = "We only want to Return Words With capital Letters";

// console.log(isCapitalized(longString).length);

// 7
// const matchMonth = (input) => {
//   let str = input.toString();
//   return str.match(/^(O?[o]?ct)(ober)?(?!\w)/i) ? true : false;
// };

// let sentence = "Hello, and have a wonderful day!";

// const noPunctuation = (str) => {
//   return str.match(/\w+ /gi);
// };

// console.log(noPunctuation(sentence));

// 9
// let string = "Ths is a regex challenge. We are trying to create a hangman phrase where all of the vowels are missing!";

// let hangman = (str) => {
//   return str.replace(/[aeiou]/gi, " ");
// };

// console.log(hangman(string));

// const seashells =
//   "She sells seashells by the seashore. The shells she sells are surely seashells. So if she sells shells on the seashore, I'm sure she sells seashore shells.";

// const findShells = (str) => {
//   return str.match(/\w+(ells)\b/gi);
// };

// console.log(findShells(seashells));

// const months = ["October", "Oct", "october", "oct", "OCTOBER", "notOctober", 123];

// const matchMonth = (input) => {
//   let str = input.toString();
//   return str.match(/^(O?[o]?ct)(ober)?(?!\w)/i) ? true : false;
// };

// console.log(months.toString());

const st = "We only Want words that Are Capitalized";

const isCapitalized = (str) => {
  return str.match(/(^[A-Z])[a-z]+/g);
};

console.log(isCapitalized(st));
