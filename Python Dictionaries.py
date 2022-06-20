dict1={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
print(dict1)
#-------------------------
dict1={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
print(dict1["brand"])
#---------------------------
dict1={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
print(len(dict1))
#-------------------------
dict1={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
print(type(dict1))
#----------------------
x={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
y = x["model"]
print(y)
#------------------------
x = {
    "name" : "Sarah",
    "family" : "blahblah",
    "birth" : 1990
}
y = x.keys()
print(y)
#--------------------------
x = {
    "name" : "Sarah",
    "family" : "blahblah",
    "birth" : 1990
}
y = x.values()
print(y)
#------------------------------
x = {
    "name" : "Sarah",
    "family" : "blahblah",
    "birth" : 1990
}
y = x.items()
print(y)
#--------------------------
x = {
    "name" : "Sarah",
    "family" : "blahblah",
    "birth" : 1990
}
y = x.get("family")
print(y)
#-----------------------;):)
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)
#-----------------------
car = {
    "brand" : "BMW",
    "model" : 630,
    "year" : 2012
}

x = car.values()
print(x)

car["year"] = 2020
print(x)
#---------------------------
car = {
    "brand" : "Benz",
    "model" : "cls",
    "year" : 2017
}
x = car.values()
print(x)

car["color"] = "red"
print(x)
#---------------------------
car = {
    "brand" : "Benz",
    "model" : "cls",
    "year" : 2017
}
x = car.items()
print(x)

car["color"] = "blue"
print(x)

car["year"] = 2021
print(x)
#------------------------------
car = {
    "brand" : "Benz",
    "model" : "cls",
    "year" : 2017
}
if "model" in car:
    print("Yes!, model is in car")
else:
    print("No!, model is not in car")

#------------------------------------
car = {
    "brand" : "Benz",
    "model" : "cls",
    "year" : 2017
}
car["year"] = 2018
print(car)
#-------------------------------
car = {
    "brand" : "Benz",
    "model" : "cls",
    "year" : 2017
}
car.update({"year":2019})
print(car)
#-----------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
car.update({"color":"white"})
print(car)
#-------------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
car.pop("year")
print(car)
#------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
car.popitem()
print(car)
#-------------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
del car["model"]
print(car)
#--------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
car.clear()
print(car)
#------------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for i in car:
    print(i)
#---------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for i in car:
    print(car[i])

#---------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for i in car.values():
    print(i)
#--------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for i in car.items():
    print(i)
#-----------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for i in car.keys():
    print(i)
#----------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
for x, y in car.items():
    print(x, y)
#-----------------------------
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
x = car.copy()
print(x)
#----------------------------
myfamily = {
    "child1": {
        "name":"Emil",
        "birth" : 2004
    },
    "child2":{
        "name":"Tobias",
        "birth":2007
    },
    "child3":{
        "name":"Linus",
        "birth":2011
    }
}
print(myfamily)
#----------------------------

child1={
    "name":"Emil",
    "birth":2004
}
child2={
    "name":"Tobias",
    "birth":2007
}
child3={
    "name":"Linus",
    "birth":2011
}
myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily)

