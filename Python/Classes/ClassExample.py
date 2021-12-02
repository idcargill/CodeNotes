class Book:
  def __init__(self, title, booktype):
    self.title = title
    if (not booktype in Book.BOOK_TYPES):
      raise ValueError('You fucked up')
    else:
      self.booktype = booktype

  
  __secret = 'I am a secret'
  
  
  # Instance Methods
  def getTitle(self):
    print(self.title)


  # Class Method (shared with all instances of a class)
  BOOK_TYPES = ('Hardcover', 'Paperback')

  @classmethod
  def getBookTypes(cls):
    return cls.BOOK_TYPES

  @classmethod
  def sayHi(cls):
    print('HELLO from Books Class')

  # Static Method (class access-no instantiation - Does not alter state)
  # Hidden (name mangled with Class name by __ default)
  @staticmethod
  def showSecret():
    if Book.__secret == None:
      return 'nothing here'
    else :
      return Book.__secret










# Instance of book
b1 = Book('Book of Sam', 'Hardcover')

b1.showSecret()
print(Book.getBookTypes())

# Class Methods work from class or with Instance
Book.sayHi()
b1.sayHi()

# Static Methods
print(Book.showSecret())

