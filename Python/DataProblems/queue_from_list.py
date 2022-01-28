arr = [ 1, 2, 3, 4, 5 ]

class Queue:
  def __init__(self):
    self.size = 0
    self.front = None
    self.tail = None

  class Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next
  
  def is_empty(self):
    return self.size == 0

  def enqueue(self, item):
    node = self.Node(item)
    if self.is_empty() == True:
      self.front = self.tail = node
      self.size += 1
    else:
      self.tail.next = node
      self.tail = node
      self.size += 1

  def get_all(self):
    if self.is_empty == False:
      return 'Nothing to see here'
    front = self.front
    results = []
    while front:
      results.append(front.value)
      front = front.next
    return results
      

  def dequeue():
    pass

def list_to_queue(list):
  q = Queue()
  for i in arr:
    q.enqueue(i)
  return q

if __name__=='__main__':
  x = list_to_queue(arr)
  print(x.get_all())
