

class Kitten:
  def __init__(self, name):
    self.name = name

  @staticmethod
  def howTo():
    print('This is how you do stuff for this class')

  def get_name(self):
    return self.name
  
  # __mehtod not accessible by other module
  def __secret_stuff(self):
    return 'i am a secret method'

  # Can access a __method
  def get_secret(self):
    print(self.__secret_stuff())

  