// Object Iteration

let person = {
  name: "Frank",
  role: "dad",
  interests: ["dad jokes", "yelling at kids", "drinking beer on the lawn"],
};

person;

let name = person.name;
name;

// For In
for (let prop in person) {
  console.log(`for in: ${prop}`);
}

// Return Arrays
let keys = Object.keys(person);
keys;

let values = Object.values(person);
values;

let entries = Object.entries(person);
entries;

console.log(entries);
