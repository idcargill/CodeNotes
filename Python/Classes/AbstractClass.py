from abc import ABC, abstractclassmethod

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


class Square(GraphicShape):
  def __init__(self, side):
    self.side = side

  def calcArea(self):
      return self.side * self.side

# g = GraphicShape() # Cannot instantiate an abstract class


c = Circle(10)      # Must overwrite abstractmethod
print(c.calcArea())  