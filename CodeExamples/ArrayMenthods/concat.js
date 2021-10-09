// Concat

// Returns new Array

/*
concat()
concat(value0)
concat(value0, value1)
concat(value0, value1, ... , valueN)
*/

const array1 = ["a", "b", "c"];
const array2 = ["d", "e", "f"];
const array3 = array1.concat(array2);

console.log(array3);
// expected output: Array ["a", "b", "c", "d", "e", "f"]

const word = "";
let newWord = word.concat("fi");
newWord = word.concat(newWord, "sh");
newWord;
