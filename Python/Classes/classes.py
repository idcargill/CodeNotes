# Classes
class Animal:
  def __init__(self, name):
    self.name = name
    self.legs = 4
    self.tail = True

class Cat(Animal):
  def talk_cat(self):
    print(f'{self.name}: meow!')
  

class Kitten(Cat):
  def __init__(self, name, weapons='claws'):
    self.name = name
    self.weapons = 'claws'


  def talk(self):
    print('I am a Kitten named {0}'.format(self.name))
    




# SUPER
Buhabuli = Kitten('Buhabuil')


print(Buhabuli.weapons)

Buhabuli.talk_cat()




