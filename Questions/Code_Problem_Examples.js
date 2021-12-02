// Method chaining
// My Attempt without chaining does not return the correct result
function urlSlugFail(title) {
  let t = title.toLowerCase().trim();
  let arr = t.split(/\s+/).join("-");
  return arr;
}

// Same Methods chained returns correct result
function urlSlug(title) {
  return title.toLowerCase().trim().split(/\s+/).join("-");
}

const x = urlSlugFail("  Winter Is    Coming");
const y = urlSlug(" Winter Is  Coming");

console.log(x);
console.log(y);

// // REGEX OR
// function spinalCase(str) {
//   return str
//     .split(/\s|_|(?=[A-Z])/)
//     .join("-")
//     .toLowerCase()
//     .trim();
// }

// console.log(spinalCase("The_Andy_Griffith_Show"));
// console.log(spinalCase("AllThe-small Things"));
// console.log(spinalCase("Teletubbies say Eh-oh"));
// console.log(spinalCase("This Is Spinal Tap"));

// FIBONACI
