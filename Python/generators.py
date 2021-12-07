# Generators // List Comprehension
'''
Created with yield statement

yield results in a generator object 
Yield remembers the state of the function after it was called. 


StopIteration will end iteration
'''


def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1

# for i in countdown():
#   print(i)


def infinite_sequence():
  num = 0
  while True:
    yield num
    num += 1

if __name__ == '__main__':
  generated = infinite_sequence()
  print(next(generated))
  print(next(generated))
  print(next(generated))






# List Comprehension
#csv = (row for row in open(file_name))
