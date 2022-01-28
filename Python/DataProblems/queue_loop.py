class Queue:
  def __init__(self):
    self.front = None
    self.tail = None
    self.size = 0

  class _Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next

  def is_empty(self):
    return self.size == 0

  def peek(self):
    return self.front.value
    
  def enqueue(self, value):
    node = self._Node(value)

    if self.front == None:
      self.front = self.tail = node
      self.size += 1     
    else:
      self.tail.next = node
      self.tail = node
      self.size += 1

  def dequeue(self):
    if self.is_empty():
      return None
    self.front = self.front.next
    self.size -= 1
    return self.front.value


# Duck Duck Goose
# Loop through a list of stings k times.  Remove the kth element each time.
def queue_loop(list, n):
  Q = Queue()
  last_value = None
  for i in list:
    Q.enqueue(i)

  for k in range(n-1):
    Q.enqueue(Q.dequeue())
  Q.dequeue()
  if Q.peek() is None:
    return last_value
  last_value= Q.peek()
  
  return last_value
         

if __name__ == '__main__':
  x = ['A', 'B', 'C', 'D', 'E']
  result = queue_loop(x, 3)
  print(result)

