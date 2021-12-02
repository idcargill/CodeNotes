class A:
  def __init__(self):
    super().__init__()
    self.foo = 'foo'
    self.name = 'Class A'


class B:
  def __init__(self):
    super().__init__()
    self.bar = 'bar'
    self.name = 'Class B'


class C(A, B):
  def __init__(self):
    super().__init__()

  def showprops(self):
    print(self.foo)
    print(self.bar)
    print(self.name)


c = C()

c.showprops()

'''
METHOD RESOLUTION ORDER
Class props are examined in the lowest level, then inherited from left to right of parent classes. 
Similar to prototype inheritance. Once a parameter is defined, no need to continue. 
'''

print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

print(C.__module__) #__main__
