import sys
from Animals import Animal
from Animals import Kat
from Animals import Kitten
from PeopleClass import *

# print(sys.version)

# Parent Class
Fred = Animal('Fred')


# Subclass
noni = Kat('Tiger')


# Subclass with own props
Fluffykins = Kitten('Fluffykins')
# Fluffykins.attack()



Ted = Student('Ted', 12)
Ted.getname()

Ted.getGrade()



Ted.sayHello()