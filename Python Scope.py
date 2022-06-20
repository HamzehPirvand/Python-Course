def myfunc():
    x = 300
    print(x)

myfunc()
#---------------
def myfunc():
    x = 400
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()
#-------------------
x = 500

def myfunc():
    print(x)

myfunc()
print(x)
#---------------
def myfunc():
    global x
    x = 450

myfunc()
print(x)
#-------------
x = 700

def myfunc():
    global x
    x = 800

myfunc()

print(x)