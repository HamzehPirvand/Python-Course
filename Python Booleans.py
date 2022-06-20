print(10 > 9)
print(10 == 9)
print(10 < 9)
#---------------
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

#-------------------------
print(bool("Hello"))
print(bool(15))
#---------------------
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#--------------------
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))
#-----------------------
def myfunction():
    return True

print(myfunction())
#------------------------
def myfunc():
    return True

if myfunc():
    print("Yes!")
else:
    print("No!")

#----------------------
x = 200
print(isinstance(x, int))