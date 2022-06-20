mytuple = ("apple", "banana", "kiwi")
print(mytuple)
#---------------------------------
mytuple = ("apple", "banana", "kiwi")
print(len(mytuple))
#-----------------------------
x = ("apple",)
y = ("banana")
print(type(x))
print(type(y))
#----------------------------------
tuple1 = ("apple", "banana", "kiwi")
tuple2 = (1, 2, 5, 7)
tuple3 = (True, False, True)
print(tuple1)
print(tuple2)
print(tuple3)
#------------------------------
mytuple = ("apple", "banana", "kiwi")
print(type(mytuple))
#-----------------------------
x = ("apple", "banana", "kiwi")
print(x[1])
#------------------------------
x = ("apple", "banana", "kiwi")
print(x[-1])
#--------------------------
fruits = ("apple", "banana", "kiwi", "mango", "melon", "orange", "cherry")
print(fruits[2:5])
#------------------------------
fruits = ("apple", "banana", "kiwi", "mango", "melon", "orange", "cherry")
print(fruits[:4])
#-------------------------
fruits = ("apple", "banana", "kiwi", "mango", "melon", "orange", "cherry")
print(fruits[2:])
#---------------------------
fruits = ("apple", "banana", "kiwi", "mango", "melon", "orange", "cherry")
print(fruits[-4:-1])
#-------------------------
mytuple = ("apple", "banana", "cherry")

if "apple" in mytuple:
    print("Yes, apple is in mytuple")

#-------------------------------------
mytuple = ("apple", "banana", "cherry")

if "kiwi" in mytuple:
    print("Yes, kiwi is in mytuple")
else:
    print("No, kiwi is not in mytuple")
#-----------------------------------
x = ("apple", "banana", "kiwi")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)
#--------------------------
x = ("apple", "banana", "kiwi")
y = ("orange",)
x += y
print(x)
#------------------------
x = ("apple", "banana", "kiwi")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#--------------------
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#------------------------
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#------------------------
mytuple = ("apple", "banana", "kiwi")

for i in mytuple:
    print(i)
#-------------------------------
mytuple = ("apple", "banana", "kiwi")
for i in range(len(mytuple)):
    print(mytuple[i])
#-------------------------------
mytuple = ("apple", "banana", "kiwi")
i = 0
while i < len(mytuple):
    print(i)
    i = i + 1
#--------------------------
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#--------------------------
fruits = ("apple", "banana", "kiwi")
mytuple = fruits * 2
print(mytuple)
#------------------------
x = (1, 2, 5, 4, 45, 62, 51, 79, 88, 34, 99)
y = x.count(7)
print(x)
#-------------------------
x = (1, 2, 5, 4, 45, 62, 51, 79, 88, 34, 99)
y = x.index(51)

print(x)
