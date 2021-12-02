// Fibonacci Problems

const testNumber = 9;

function fib(num) {
  if (num <= 1) {
    return num;
  }
  return fib(num - 1) + fib(num - 2);
}

let fibx = fib(testNumber);
// console.log(fibx);

function fibCheck(num) {
  if (num <= 1) {
    return num;
  }
  return fibCheck(num - 2);
}

let fibCheckx = fibCheck(testNumber);
// console.log(fibCheckx);

// Store previous num values
function fib2(num) {
  let a = 0,
    b = 1,
    c;
  for (let i = 2; i < num; i++) {
    if (i === num) {
      return num;
    }
    c = a + b;
    a = b;
    b = c;
    console.log(b);
  }
  return b;
}

// console.log(fib2(testNumber));

// PRIME NUMBERS
function sumPrimes(num) {
  return num;
}

function isPrime(num) {
  let sq = Math.round(Math.sqrt(num) + 1);
  if (sq % 2 === 0) {
    console.log(sq);
    return "prime";
  }
  return "not prime";
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(nums.map((n) => isPrime(n)));
