# LISTS

# Slice
'''
list[start:end:step]

list[:end:step]

list[::-1] #reverse 
'''






# SETS
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

print(a)