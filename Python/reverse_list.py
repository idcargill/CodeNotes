#input 
x = [ 'a', 'b', 'c', 'd']
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# output 'd', 'c', 'b', 'a'

def reverse_list(lst):
  # for i in range( len(lst) // 2 ):
  #   lst[i] = lst[-1 -i]
  #   lst[-1 -i] = lst[i]
  # return lst
  
  for i in range(len(lst) // 2):
    lst[i], lst[-1 - i] = lst[-1 - i], lst[i]      
    return lst
  





y = reverse_list(digits)
print(y)    




# Reverse Linked List
# input[ 'a', 'b', 'c', 'd']

# output 'd', 'c', 'b', 'a'


# >>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# >>> for i in range(len(digits) // 2):
# ...     digits[i], digits[-1 - i] = digits[-1 - i], digits[i]
# ...

# >>> digits
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]