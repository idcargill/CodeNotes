# Decorators
# A way to modify functions with other functions.

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


### Function / Decorators
# Functions are first class
def process(bool):
  def do_true_things():
    return 'I am a True thing'

  def do_false_things():
    return 'I am a False thing'

  return do_true_things if bool else do_false_things


decorated_func = process(False)

print(decorated_func())


## 
def modify_and_do_twice(func):
  def wrapper(*args, **kwargs):
    if 'yes' in args:
      print('Wrapper function is triggering passed in func')
      func(*args, **kwargs)
      func(*args, **kwargs)
  return wrapper

@modify_and_do_twice
def run_code(i):
  print(i)

print(run_code('yes'))

## Returning function
def do_twice(func):
  def wrapper(*args, **kwargs):
    func(*args,*kwargs)
    func(*args,*kwargs)
  return wrapper

@do_twice
def add_stuff(x,y):
  return x + y


## Returning Value
def my_decorator(func):
  def wrapper(*args, **kwargs):
    # do stuff in wrapper then return value
    return func(*args, **kwargs)
  return wrapper

@my_decorator
def make_important(word):
  return word + '!!'

print(make_important('Cats'))




# Class Decorators: 
# Modifying a Class constructor
def modify_class(cls):
  def wrapper(*args, **kwargs):
    n = cls(*args, **kwargs)
    n.special_new_prop = 'Fluffykins'
    return n
  return wrapper
@modify_class
class Animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type

kitten = Animal('Noni', 'Tiger')

print(kitten.special_new_prop)