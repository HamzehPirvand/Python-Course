mylist = ["apple", "banana", "orange"]
mylist.append("kiwi")
print(mylist)
#------------------
mylist = ["apple", "banana", "kiwi"]
mylist.insert(1, "melon")
print(mylist)
#------------------------
mylist = ["apple", "banana", "orange"]
thislist = ["kiwi", "melon", "cherry"]
mylist.extend(thislist)
print(mylist)
#-------------------------
mylist = ["kiwi", "orange", "banana"]
list1 = ("apple", "melon")
mylist.extend(list1)
print(mylist)
#----------------------------
mylist = ["apple", "banana", "kiwi"]
mylist.remove("banana")
print(mylist)
#------------------------------
mylist = ["banana", "apple", "melon"]
mylist.pop(1)
print(mylist)
#------------------------------
mylist = ["banana", "apple", "melon"]
mylist.pop()
print(mylist)
#------------------------------
mylist = ["apple", "banana", "cherry"]
del mylist[1]
print(mylist)
#--------------------------
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)
#----------------------
mylist = ["apple", "banana", "cherry"]

for i in mylist:
    print(i)

#-----------------------------
mylist = ["apple", "banana", "cherry"]

for i in range(len(mylist)):
    print(mylist[i])

#----------------------------
mylist = ["apple", "banana", "cherry"]

i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1
#------------------------------------
mylist = ["apple", "banana", "cherry"]

i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 2

#-------------------------------------
mylist = ["apple", "banana", "cherry"]

i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 3

#------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)

print(newlist)
#-------------------------------------
mylist = ["orange", "mango", "apple", "kiwi", "banana", "mango", "melon"]
mylist.sort()
print(mylist)
#---------------------------------------
list1 = [84, 95, 2, 34, 17, 29, 0, 1]
list1.sort()
print(list1)
#-----------------------------------
mylist = ["orange", "mango", "apple", "kiwi", "banana", "mango", "melon"]
mylist.sort(reverse=True)
print(mylist)
#--------------------------------
list1 = [84, 95, 2, 34, 17, 29, 0, 1]
list1.sort(reverse=True)
print(list1)
#-----------------------------
mylist = ["orange", "mango", "apple", "kiwi", "banana", "mango", "melon"]
mylist.sort(key= str.lower)
print(mylist)
#------------------------------
list2 = ["apple", "kiwi", "banana", "cherry"]
list2.reverse()
print(list2)
#-------------------------
list1 = ["apple", "banana", "cherry"]
mylist = list1.copy()
print(mylist)
#----------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#------------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
#---------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#--------------------------
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "kiwi")
print(fruits)
#------------------------
fruits = ["apple", "banana", "cherry"]
x = fruits.index("cherry")
print(x)
#--------------------------
fruits = ["apple", "banana", "cherry"]
x = fruits.count("apple")
print(x)

