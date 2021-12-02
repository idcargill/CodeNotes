/*

slice() - find elements in an array
not modified

splice(start, length to replace, newValue) - replaces parts of an array
is modified

split() - Turn strings into arrays
not modified

join() - Turn arrays into strings
not modified

*/

let text = "This was a good idea";

let split = text.split(" ");
split;
text;

let j = split.join(" ");
j;

let slice = text.slice(2, 15);
slice;

//
let list = ["fish", "cat", "shark", "dog"];
list.splice(0, 2, "lion");
list;
