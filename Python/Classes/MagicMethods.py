class Book:
  def __init__(self, title, author, price):
    super().__init__()
    self.title = title
    self.author = author
    self.price = price
    self._discount = 0.2


  ## MAGIC __str__ method to return a string
  def __str__(self):
    return F'{self.title} by {self.author} that costs {self.price}'

  ## MAGIC __repr__ method to return an obj representation
  def __repr__(self):
    return F'title={self.title}, author={self.author}, price={self.price}'

  ## MAGIC method checks for equality between two objects
  def __eq__(self, value):
    if not isinstance(value, Book):
      raise ValueError('Can\'t compare none book item')
    return (self.title == value.title and 
    self.author == value.author and
    self.price == value.price)
  
  ## MAGIC method checks for greater than or equal
  def __ge__(self, value):
    if not isinstance(value, Book):
      raise ValueError('Can\'t compare a non-book')
    return self.price >= value.price

  ## MAGIC method checks for less than
  def __lt__(self, value):
    if not isinstance(value, Book):
      raise ValueError('Can\'t compare a non-book')
    return self.price < value.price

  ## MAGIC __getattribute__ called when attr is retrieved
  def __getattribute__(self, name):
    if name == 'price':
      p = super().__getattribute__('price')
      d = super().__getattribute__('_discount')
      return p - (p * d)
    return super().__getattribute__(name)

  ## MAGIC __setattr__ 
  def __setattr__(self, name, value):
    if name == 'price':
      if type(value) is not float:
        raise ValueError('Price attribute must be float')
    return super().__setattr__(name, value)

  ## MAGIC __getattr__ called when __getattribute__ lookup fails
  # def __getattribute__(self, name):
  #   return name + ' is not here'

  ## MAGIC __call__ call and object like a function
  def __call__(self, title, author, price):
    self.title = title
    self.author = author
    self.price = price






b1 = Book('War and Peace', 'Leo Tolstoy', 39.95)
b2 = Book('Hamburger Man', 'Frank', 22.95)
b3 = Book('Hamburger Man', 'Frank', 22.95)
# print(b2.__repr__())
# print(str(b2))
# print(b2)

# print(b1.__str__())
# print(b1)           # uses the __str__ method by default for output




##############
## Equality and Comparison Magic Methods
# print(b2 == b3 )
# print(b1 == b2)
# print(b1 == 'cat')

# print(b2 > b1)



# Attribute Access  __getattribute__   Must call value from super class __getattribute__ to avoid circular reference
# print(b1) # discount is applied when price attribute is called


# Set Attribute __setattr__
b1.price = 50.3
# print(b1.price)

# __getattr__   Returns when attribute is not found. 
# print(b1.cats)

# __call__ Call an instance like a function.  Can not use with __getattr__
b1('Santa eats cats', 'Dude from the north', 44.0)
print(b1)


