from random import randint

arr = [ 1, 2, 3, 4, 5]


new_list = [i * 10 for i in arr ]
print(new_list)


random_numbers = [ randint(1,6) for i in range(10)]
print(random_numbers)


even_nums = [x for x in range(10) if x % 2 == 0]
print(even_nums)

names = ['Toshi', 'Mike', 'Vanessa']
letters = [ name[:3] for name in names ]
print(letters)


modified = [x+y for x in ['Cat', 'hat', 'bat'] for y in ['!', '?', '.']]
print(modified)



### Function / Decorators

def process(bool):
  def do_true_things():
    return 'I am a True thing'

  def do_false_things():
    return 'I am a False thing'

  return do_true_things if bool else do_false_things


decorated_func = process(False)

print(decorated_func())



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


def my_decorator(func):
  def wrapper(*args, **kwargs):
    # do stuff in wrapper then return value
    return func(*args, **kwargs)
  return wrapper

@my_decorator
def make_important(word):
  return word + '!!'

print(make_important('Cats'))



## Return a wrapper function
def repeater(num_times):
  def wrapper_reapeat(func):
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        print(func(*args,**kwargs))
    return wrapper
  return wrapper_reapeat 

@repeater(5)
def say_something(word):
  return word

say_something('hi')


# Class Decorators: Modifying a Class constructor
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
