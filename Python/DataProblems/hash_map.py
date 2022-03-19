
class HashMap:
  def __init__(self):
    self.MAX = 10
    self.array = [[] for n in range(self.MAX)]

  def hash(self, key):
    total = 0
    for i in key:
      total += ord(i)
    return total % self.MAX

  def __setitem__(self, key, value):
    h = self.hash(key)
    for item in self.array[h]:
      if item[0] == key:
        raise Exception('Collision Allert')
    self.array[h].append((key, value))

  def __getitem__(self, key):
    h = self.hash(key)

    if len(self.array[h]) == 0:
      return None

    for i in self.array[h]:
      if i[0] == key:
        return i[1]


  def __str__(self):
    text = ''
    for i in self.array:
      if len(i) > 1:
        for j in i:
            text += f'{j[0]} : {j[1]}\n'
      else:
        if len(i) > 0:
          text += f'{i[0][0]} : {i[0][1]}\n'
    return text

  def set_item(self, key, value):
    h = self.hash(key)
    found = False
    # key already exists
    for idx, element in enumerate(self.array[h]):
      if len(element) == 2 and element[0]==key:
        self.array[h][idx] = (key, value)
        found = True
        break
    if not found:
      self.array[h].append((key, value))



# ord returns unicode character

h = HashMap()

h['fish'] = 10
h['dog'] = 20
h['god'] = 300

# h.set_item('fish', 10)
# h.set_item('dog', 20)
# h.set_item('god', 300)

h['salmon'] = 1000
print(h.array)

print(h['dog'])
print(h['nothing'])


print(h)