import os

class Person:
  def __init__(self, name):
      self.name = name

  def getname(self):
    print(self.name)
  
  __PeopleList = None

  # Static method
  @staticmethod
  def getPeopleList():
    if Person.__PeopleList == None:
      Person.__PeopleList = []
    else:
      return Person.__PeopleList 

  @classmethod
  def sayHello(cls):
    print(f'I am a class method that knows who {cls.name} is')

class Student(Person):
  def __init__(self, name, grade):
    super().__init__(name)
    self.grade = grade

  def getGrade(self):
    print(F'I, {self.name} am in {self.grade} grade')

  


### Inheritance From Vehicle
class Vehicle:
  def __init__(self, wheels):
    self.wheels = wheels

  def drive(self):
    print('VROOOOOOM!')

  def honk(self):
    print('beep beep!')


## Subclass
class Car(Vehicle):
  def __init__(self, wheels, color): 
    super().__init__(wheels) # pass up to super arguments
    self.color = color
    self.wheels = wheels - 1

  def __str__(self):
    return f'The saturn has {self.wheels} wheels and is {self.color}.'

  def __repr__(self):
    return f'Car(wheels={self.wheels}, color={self.wheels})'

saturn = Car(4, 'grey')

saturn.honk()
saturn.drive()
print(saturn.wheels)

print(saturn.__str__())
print(saturn.__repr__())





## Static and Class Methods
## State held in Class, accessed with classmethods

class Parent:
  def talk(self):
    print(self.name)

  @staticmethod
  def damn_kids():
    print('Get off my lawn!')

class Child(Parent):
  total_children = 0

  def __init__(self, name):
    self.name = name

    Child.total_children += 1 

  @classmethod
  def get_children_count(cls):
    print(cls.total_children)
  
Frank = Child('Fluffy')
Dude = Child('Stupid')
Frank.talk()
Frank.get_children_count()

Daddy = Parent()
Daddy.damn_kids()


Frank.damn_kids()