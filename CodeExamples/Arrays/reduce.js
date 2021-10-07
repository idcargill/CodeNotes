// Reduce
// Returns the last version of the accumulator

// arr.reduce((accumulator, value, index) => accumulator + value);

let people = [
  { name: "Fred", role: "Developer" },
  { name: "Suzy", role: "Developer" },
  { name: "Gina", role: "Manager" },
  { name: "Jim", role: "Support" },
];

let folks = people.reduce((accumulator, person, idx) => {
  accumulator[person.name] = person.role;
  return accumulator;
}, {});

// folks:
// {
//   Fred: 'Developer',
//   Suzy: 'Developer',
//   Gina: 'Manager',
//   Jim: 'Support'
// }
// console.log(folks);

const numbers = [1, 2, 3, 4, 5, 6, 7];

// starting value optional
const newthing = numbers.reduce((accumulator, val, idx) => {
  return accumulator + val;
}, 2);

// console.log(newthing);
