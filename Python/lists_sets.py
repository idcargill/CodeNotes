# LISTS

# Slice
'''
Methods
list.append(x)
list.extend(iterable)
list.insert(i, x)
list.remove(x)
list.pop(i)
list.clear()
list.index()
list.count(x) # times x shows up in list
list.sort()
list.reverse()
list.copy()   returns shallow copy


# Slicing
list[start:end:step]

list[:end:step]

list[::-1] #reverse 

# List as Stack
.append()
.pop()

# list as Queue
from collections import deque
deque.append()
deque.popleft()

'''

# List Comprehension
squares = []
for x in range(10):
  squares.append(x**2)
print(squares)




### SETS
num_set = {1, 2, 3, 4, 5}
'''
Sets are unordered, 

Set Methods
  len
  set.add('a')
  set.remove('a')
  set.pop(arbitrary element)


  | union operator combines 2 sets
  & intersection gets items in both sets
  - difference gets items in first set but not in second
  ^ symmetric difference gets items in either set but not both

'''
set1 = { 1, 2, 3}
set2 = { 1, 2, 5,7,9 }

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)


# What is the result of this code?
def power(x, y):
  if y == 0:
    return 1
  else:
    print(x * y)
    return x * power(x, y-1)
		
print(power(2, 3))


a = (lambda x: x * (x+1)) (6)



### Tuples
# immutable


