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

Daddy = Parent()
print(Daddy)

Daddy.damn_kids()

Frank.get_children_count()