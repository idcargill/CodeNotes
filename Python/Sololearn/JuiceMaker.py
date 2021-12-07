class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, x):
      name = F'{self.name}&{x.name}'
      cap = self.capacity + x.capacity
      return F'{name} ({cap}L)'


    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)










#num=10
#print(num.__add__(10))

