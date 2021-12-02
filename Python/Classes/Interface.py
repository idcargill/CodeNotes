# INTERFACE
from abc import ABC, abstractclassmethod


class JSONify(ABC):     
  @abstractclassmethod
  def toJSON(self):
    pass



# Inherit abstract base class
class GraphicShape(ABC):
  def __init__(self):
    super().__init__()

  @abstractclassmethod   #Decorator
  def calcArea(self):
    pass


class Circle(GraphicShape):
  def __init__(self, radius):
    self.radius = radius

  def calcArea(self):
    return 3.14 * (self.radius ** 2)

  def toJson(self):
    return f'{{ "square" : {str(self.calcArea())} }}'





c = Circle(10)
print(c.calcArea())

print(c.toJson())

'''
Abstractclassmethods force you to overwrite the method.
Force subclasses to define a toJson() method

Applything the JSONify "interface" to require specific methods
'''