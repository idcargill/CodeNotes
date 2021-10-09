let line1 = "Start ";
let line2 = "End";

let story = line1 + line2;
story;

let obj1 = { animals: "tiger", food: "people" };
let obj2 = { animals: "kitten" };

let obj3 = { ...obj1, ...obj2 };
obj3;

let obj4 = { ...obj1 };
obj4;
obj4.weapon = "claws";

obj3;
obj4;

let u = undefined;
let nope = null;
let int = 50;
let int2 = new Number(50);

int;
int2;

u;
int;
nope;

let test = nope == u ? "so equal" : "not equal";
test;

let max = Number.MAX_VALUE;
max;

let BigMax = Number.MAX_SAFE_INTEGER;
BigMax;

let min = Number.MIN_VALUE;
min;

let x = obj4.x;
