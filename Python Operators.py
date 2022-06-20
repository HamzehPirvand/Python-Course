print(10+5)
#----------------
x = 5
y = 7
print(x+y)
#----------------
x = 5
y = 2
print(x - y)
#----------------
x = 5
y = 3
print(x * y)
#-----------------
x = 12
y = 3
print(x / y)
#-----------------
x = 5
y = 2
print(x % y)
#------------------
x = 2
y = 5
print(x ** y)
#----------------
x = 5

x += 3
print(x)
#------------------
x = 5

x -= 3
print(x)
#-----------------
x = 5

x *= 2
print(x)
#---------------
x = 6

x /= 4
print(x)
#--------------------
x = 5

x %= 2
print(x)
#--------------------
x = 5

x |= 3
print(x)
#-------------------
x = 2

x **= 10
print(x)
#--------------------
x = 5
y = 3

print(x == y)
#-----------------
x = 5
y = 3

print(x != y)
#--------------------
x = 5
y = 3

print(x > y)
#------------------------
x = 5
y = 3

print(x < y)
#-------------------------
x = 5
y = 3

print(x >= y)
#--------------------
x = 5
y = 3

print(x <= y)
#----------------------
x = 5

print(x > 3 and x < 10)
#----------------------
x = 5

print(x > 3 or x < 4)
#---------------------
x = 5

print(not(x > 3 and x < 10))
#----------------------------
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#--------------------------
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not y)
print(x is not z)
print(x != y)
#-------------------
x = ["banana", "apple"]

print("banana" in x)
#---------------------
x = ["banana", "apple"]

print("banana" not in x)
