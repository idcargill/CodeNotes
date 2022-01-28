import os
import sys


# sys.path.append(os.path.join(os.path.dirname('__file__'), '../'))
# print(sys.path)

from linked_lists.linked_list_single import LinkedList

arr = []
for i in range(10):
  arr.append(i)

def sum_odd_values(list):
  sum = 0
  for i in arr:
    if i % 2 == 1:
      sum += i
  return sum


print(f'Sum of odd values: {sum_odd_values(arr)}')


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)


def sum_odd_linkedList(LL):
  sum = 0
  curr = LL.head
  while curr:
    if curr.value % 2 == 1:
      sum += curr.value
    curr = curr.next
  return sum

print(f'Sum odd linked list: {sum_odd_linkedList(LL)}')