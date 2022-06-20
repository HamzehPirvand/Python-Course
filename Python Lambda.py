x = lambda a : a + 10
print(x(5))
#----------------------
x = lambda a, b : a + b
print(x(5, 7))
#-----------------------
x = lambda a, b : a * b
print(x(4, 8))
#----------------------
x = lambda a, b, c : a + b + c
print(x(10, 11, 14))
#----------------------
x = lambda a, b : a / b
print(x(10, 2))
#-----------------------
x = lambda a, b : a - b
print(x(12, 8))
#-------------------------
def myfunc(n):
    return lambda a : a * n

x = myfunc(2)

print(x(11))
#------------------------
def myfunc(n):
    return lambda a : a * n

x = myfunc(5)
y = myfunc(6)

print(x(8))
print(y(9))
