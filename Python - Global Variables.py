x = "awesome"

def myfunc():
    print("python is " + x)

myfunc()
#----------------------
x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is " + x)

myfunc()

print("python is " + x)
#---------------------------
def myfunc():
    global x
    x = "Great"

myfunc()

print("python is " + x)
#-----------------------------
x = "Quik"

def myfunc():
    global x
    x = "Best"

myfunc()

print("python is " + x)
