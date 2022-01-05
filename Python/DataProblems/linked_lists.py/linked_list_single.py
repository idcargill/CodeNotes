class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def getValue(self):
    return self.value

  def getNext(self):
    return self.next

  def setNext(self, newData):
    self.next = newData



class LinkedList:
  def __init__(self, head=None):
    self.head = head
    self._size = 0

  def getHead(self):
    return self.head

  def insert(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    self._size += 1
 

  def includes(self):
    pass

  def to_string(self):
    pass



ll = LinkedList()
ll.insert('Frank')
ll.insert('Tom')
ll.insert('Cats')


print(ll.head.value)
print(ll.head.next.value)

# LL = []
# LL.insert(n1)
# LL == [ n1 ]    head n1
# LL.insert(n2)   
# LL == n2 -> n1  head n2
# LL.insert(n3)
# LL == n3 -> n2 -> n1  head n3