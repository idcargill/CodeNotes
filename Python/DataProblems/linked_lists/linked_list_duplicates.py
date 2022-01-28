from linked_list_single import LinkedList, Node

L1 = LinkedList()
L2 = LinkedList()

L1.insert(1)
L1.insert(5)
L1.insert(6)
L1.insert(7)
L1.insert(8)

for i in range(10):
  L2.insert(i)

def find_duplicate_values(L1, L2):
  p1 = L1.head
  p2 = L2.head
  results = []

  while p1:
    if L2.includes(p1.value):
      results.append(p1.value)
      p1 = p1.next
  return results


if __name__ == '__main__':
  x = find_duplicate_values(L1, L2)
  print(x)