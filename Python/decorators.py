# Decorators

'''
A way to modify functions with other functions.

'''

def sayHi():
  print('hello')

def decorator(func):
  print('#' * 5)
  func()
  print('#' * 5)

decorated = decorator(sayHi)


# @ symbol references a decorator

@decorator
def hello():
  print('This is hello again')

hello()
