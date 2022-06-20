tuple1 = ("apple", "banana", "kiwi")

myiter = iter(tuple1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
#------------------------
mystr = ("banana")

myiter = iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#------------------------
mytuple = ("apple", "banana", "kiwi")

for i in mytuple:
    print(i)
#-------------------------
mystr = ("kiwi")

for i in "kiwi":
    print(i)

#--------------------------
str1 = ("cherry")

for x in str1:
    print(x)

#----------------------------
class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#----------------------
class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = mynumber()
myiter = iter(myclass)


for x in myiter:
    print(x)