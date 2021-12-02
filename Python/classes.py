# Classes

class Cat:
  def __init__(self, name):
    self.name = name
    self.color = 'grey'

  def speak(self):
    print('My name is {0}, Meow! I am {1}'.format(self.name, self.color))

  def eat(self):
    print('crunch crunch crunch')

noni = Cat('Noni')

noni.speak()



# Inheritance
class Kitten(Cat):
  def talk(self):
    print('I am a Kitten named {0}'.format(self.name))
    
Tiger = Kitten('Fluffykins')
Tiger.talk()



# SUPER

Buhabuli = Kitten('Buhabuil')



import sys 
print(sys.version)