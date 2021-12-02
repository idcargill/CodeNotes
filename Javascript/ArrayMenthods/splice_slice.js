// Slice - String or Array
// Does not change original array
// slice(start index, End Index)  end not inclusive

let text = "The cat is hungry and ate the shark.";

let slicedText = text.slice(0, 4);
console.log(slicedText, "\n", text);

let fromEnd = text.slice(-6);
console.log(fromEnd);

let arr = [1, 2, 3, 4, 5, 6];
let newArr = arr.slice(1, 3);
console.log(arr, "\n", newArr);

//
// Splice  - Array
// Changes original array
// splice.(start index, # of items, replacement values)
// returnes the removed elements

let text2 = ["cat", "hat", "shark", "people"];

let spliceText2 = text2.splice(2, 1, "crunchies", "fat", "chunky", "ice cream");
spliceText2;
console.log(text2, "\n", spliceText2);
