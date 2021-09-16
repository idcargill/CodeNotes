// Constructor Funtions and Prototypes
// ()=> not allowed for constructors
// Constructor.call(this, ...args) then attach prototype

// const Animal = function (name, legs) {
// 	this.name = name;
// 	this.legs = legs;
// 	this.eat = function () {
// 		this.eating = true;
// 	};
// };

// Animal.prototype.walk = function () {
// 	this.isWalking = true;
// };

// Animal.prototype.sing = function () {
// 	console.log('La la la la laaaaa');
// };

// const Dog = function (name, legs) {
// 	Animal.call(this, name, legs);
// };
// Dog.prototype = Object.create(Animal.prototype);

// let puppy = new Dog('Frank', 3);

// puppy.walk();
// puppy.eat();
// puppy.sing();

// console.log(puppy);

// console.log(Animal.prototype);

// console.log(puppy instanceof Animal); // true
// console.log(puppy instanceof Dog); // true

// ES6 Classes ===========================================

class Animal {
	constructor(name, legs) {
		this.name = name;
		this.legs = legs;
	}

	walk() {
		this.isWalking = true;
	}

	eat() {
		this.isEating = true;
	}
}

class Dog extends Animal {
	constructor(name, legs, fur) {
		super(name, legs);
		this.fur = fur;
	}

	speak() {
		console.log('WOOF!');
	}
}

let rosie = new Dog('Rosie', 3, 'short');
let frank = new Animal('Frank', 10);

rosie.walk();
rosie.eat();
rosie.speak();

console.log(rosie);

frank.eat();

console.log(frank);
