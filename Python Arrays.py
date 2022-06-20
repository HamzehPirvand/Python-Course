cars = ["BMW", "Benz", "Volvo"]

x = cars[0]
print(x)
#------------------------
cars = ["BMW", "Benz", "Volvo"]

cars[0] = "Toyota"
print(cars)
#----------------------
cars = ["BMW", "Benz", "Volvo"]

x = len(cars)
print(x)
#-----------------
cars = ["BMW", "Benz", "Volvo"]
print(len(cars))
#----------------------
cars = ["BMW", "Benz", "Volvo"]
for x in cars:
    print(x)
#------------------
cars = ["BMW", "Benz", "Volvo"]

cars.append("Honda")
print(cars)
#------------------
cars = ["BMW", "Benz", "Volvo"]

cars.remove("BMW")
print(cars)
#----------------------
fruits = ["apple", "banana", "kiwi", "cherry"]

fruits.clear()
print(fruits)
#--------------------------
fruits = ["apple", "banana", "kiwi", "cherry"]

x = fruits.copy()
print(x)
#---------------------------
fruits = ["apple", "kiwi", "mango", "melon"]

x = fruits.count("kiwi")
print(x)
#----------------------------
points = [1, 2, 3, 4, 5, 8, 9, 7, 6]

x = points.count(9)
print(x)
#------------------------
fruits = ["apple", "kiwi", "mango", "melon"]
cars = ["volvo", "ford", "Honda", "Toyota"]

fruits.extend(cars)
print(fruits)
#----------------------------
fruits = ["apple", "melon", "mango", "kiwi"]

x = fruits.index("kiwi")
print(x)
#-------------------
cars = ["Honda", "volvo", "Toyota", "BMW"]

cars.insert(1, "ford")
print(cars)
#--------------------
fruits = ["apple", "banana", "cherry"]

fruits.reverse()
print(fruits)
#-------------------
cars = ["ford", "volvo", "BMW", "Honda"]

cars.sort()
print(cars)
#-------------
cars = ["ford", "volvo", "BMW", "Honda"]

cars.sort(reverse=True)
print(cars)
#---------------------
def myfunc(x):
    return len(x)

cars = ["ford", "BMW", "VW", "Mitsubishi"]
cars.sort(key=myfunc)
print(cars)
#------------------------
def myfunc(x):
    return x["year"]

cars = [
    {"car" : "ford", "year" : 1964},
    {"car" : "BMW", "year" : 2000},
    {"car" : "VW", "year" : 2005},
    {"car" : "Volvo", "year" : 2017}
]

cars.sort(key=myfunc)
print(cars)