// SPLIT
// String to Array
// does not modify original

let string = "This is text about pumpkins.";
let newString = string.split(); // spaces by deafault
string;
newString;

newString2 = string.split(""); // each char
newString2;

newString3 = string.split("t"); // split on 't'
newString3;

// JOIN
// Array to a string
// Does not modify original
// join(char to join with)  comma by default

let arr = ["This", "is", "a", "story", "about", "Fred"];
arr;
let newArr = arr.join();
arr;
newArr;

let newArr1 = arr.join(" ");
arr;
newArr1;

let newArr2 = arr.join(" #");
arr;
newArr2;
