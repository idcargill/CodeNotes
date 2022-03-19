// FOR LOOP
console.log('\nfor loop')
// for loop
for ( let a = 0; a < 5; a++) {
  console.log('\t',a)
}

// WHILE
console.log('\nwhile loop')
let b = 0;
while (b < 5) {
  console.log('\t',b)
  b += 1
}



// DO WHILE
console.log('\nDo while')





// FOR EACH
console.log('\nFor Each Loop: on array')
let array = ['cat', 'bat', 'hat']
array.forEach(i => console.log('\t',i))

// MAP
console.log('\nMap')
let mapArray = ['cat', 'bat', 'hat']
let newArr = mapArray.map(i => i)
console.log('\t',newArr)

// FOR IN  ( objects )
console.log('\nFOR IN: object')
const obj = { name: 'frank', job: 'broom pusher'};
for (item in obj) {
  console.log(`\t${item} : ${obj[item]}`)
}

// FOR OF ( array )
console.log('\nFOR OF: array')
for (let item of array) {
  console.log('\t',item)
}
