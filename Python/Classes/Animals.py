class Animal:
  def __init__(self, name):
    self.name = name

  def walk(self):
    print('walking around')

  def talk(self):
    print('Hello I am an animal')


# Subclass with same props as parent
class Kat(Animal):
  pass


# Subclass with added props
class Kitten(Animal):
  def __init__(self, name):
    self.name = name
    self.claws = 50
    
  def attack(self):
    print(F'I, {self.name} hear by claw your face off!')

  

