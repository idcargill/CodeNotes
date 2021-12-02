class Publication:
  def __init__(self, title, price):
    self.title = title
    self.price = price

  def getTitle(self):
    print(self.title)

  def showPrice(self):
    print(self.price)

  @staticmethod
  def sayHello():
    print('Hi Everybody!')


class Periodical(Publication):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price)
    self.period = period
    self.publisher = publisher


class Book(Publication):
  def __init__(self, title, price, author, pages):
    super().__init__(title, price)
    self.author = author
    self.pages = pages


class Magazine(Periodical):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price, period, publisher)


class NewsPaper(Periodical):
  def __init__(self, title, price, period, publisher):
    super().__init__(title, price, period, publisher)


####
b1 = Book('Harry', 50, 'Frank', 100)

n1 = NewsPaper('PI', 1.25, 'Daily', 'Frank')

# Static method call
Publication.sayHello()
n1.sayHello() 