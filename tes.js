console.time()
console.group();

const z = shark;
debugger;

const x = { name: 'cat', food: 'crunchies'};
console.log(x)

let y = Object.assign(x, {hungry: true});

setTimeout(()=> {
  console.log(y);
  console.timeLog();
},3000);
