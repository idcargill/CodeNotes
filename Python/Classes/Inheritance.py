class Publication:
  def __init__(self, title, price):
    self.title = title
    self.price = price

  def getTitle(self):
    print(self.title)

  def showPrice(self):
    print(self.price)

  @staticmethod
  def sayHello():
    print('Hi Everybody!')


class Periodical(Publication):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price)
    self.period = period
    self.publisher = publisher


class Book(Publication):
  def __init__(self, title, price, author, pages):
    super().__init__(title, price)
    self.author = author
    self.pages = pages


class Magazine(Periodical):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price, period, publisher)


class NewsPaper(Periodical):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price, period, publisher)


####
b1 = Book('Harry', 50, 'Frank', 100)

n1 = NewsPaper('PI', 1.25, 'Daily', 'Frank')

# Static method call
Publication.sayHello()
n1.sayHello() 



# PERSON =================================
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
  _counter = 0

  def __init__(self, wheels, color): 
    super().__init__(wheels) # pass up to super arguments
    self.color = color
    self.wheels = wheels - 1

    Car._counter += 1

  @staticmethod
  def how_many_cars():
    print(f'There are {Car._counter} cars instantiated')

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

golf = Car(4, 'white')


library = {
  'name': 'Frank',
  'dude': 'not Frank',
  'Huba': 'fucking idiot'
}
print(library.__repr__())



Car.how_many_cars()