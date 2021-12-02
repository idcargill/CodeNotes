class Person:
  def __init__(self, name):
      self.name = name

  def getname(self):
    print(self.name)
  
  __PeopleList = None

  # Static method
  @staticmethod
  def getPeopleList():
    if Person.__PeopleList == None:
      Person.__PeopleList = []
    else:
      return Person.__PeopleList 

  @classmethod
  def sayHello(cls):
    print(f'I am a class method that knows who {cls.name} is')





class Student(Person):
  def __init__(self, name, grade):
    super().__init__(name)
    self.grade = grade

  def getGrade(self):
    print(F'I, {self.name} am in {self.grade} grade')

  