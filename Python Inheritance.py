class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = person("John", "Doe")
x.printname()
#-----------------------
class person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    pass

x = student("Mike", "Olsan")
x.printname()
#------------------------------------
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#----------------------------------
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname):
        super(). __init__(fname, lname)

x = student("Joe", "Olsan")
x.printname()
#----------------------------
class father:
    def __init__(self, lname, face, height, personallity):
        self.lname = lname
        self.face = face
        self.height = height
        self.personallity = personallity

    def printname(self):
        print(self.lname, self.face, self.height, self.personallity)

class son(father):
    def __init__(self, lname, face, height, personallity):
        super(). __init__(lname, face, height, personallity)

x = son("Olsan", "look like father", "180 cm", "look like father")
x.printname()
#-------------------------------
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname, year):
        super(). __init__(fname, lname)
        self.graduationyear = year

x = student("Mike", "Olsan", 2020)
print(x.graduationyear)
#------------------------------
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname, year):
        super(). __init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)

x = student("Sarah", "Olsan", 2021)
x.welcome()
