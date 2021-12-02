// Constructor Function  requires new
// tagging on prototypes

// Constructor Functions
// - bind this within the constructor
// - binds instance._proto_ to Constructor.prototype
// - binds instance._proto_.constructor to Constructor
// - implicitly returns this, which refers to instance

function CarConstructor() {}

CarConstructor.prototype.drive = function () {
  console.log("Vroom");
};
let car = new CarConstructor();
car.drive();

// Constructor Function (classes ARE constructor functions)
// requires new
const Kitten = function (name) {
  this.name = name;
  this.food = "crunchies";
};

const Noni = new Kitten("noni");
console.log(Noni);

const Fluffykins = Kitten("Fluffykins");

// Factory Function.  Returns and object.  new not required
const personFactory = (name, age) => {
  const sayHello = () => console.log("hi");
  return { name, age, sayHello };
};

const frank = personFactory("frank", 31);
frank.sayHello();
console.log(frank);
//================

// Constructor
const Person = function (name, age) {
  this.name = name;
  this.age = age;
  this.sayHello = () => console.log("hello");
};

const me = new Person("ian", 41);
me.sayHello();
