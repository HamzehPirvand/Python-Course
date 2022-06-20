myset = {"apple", "banana", "kiwi"}
print(myset)
#------------------------------
myset = {"kiwi", "melon", "mango"}
print(len(myset))
#-----------------------------
myset = {"kiwi", "mango", "melon"}
print(type(myset))
#---------------------
myset = {"kiwi", "mango", "melon"}

for i in myset:
    print(i)

#---------------------------
myset = {"kiwi", "melon", "mango"}
print("melon" in myset)
#-------------------------------
myset = {"kiwi", "melon", "mango"}
myset.add("orange")
print(myset)
#--------------------------
set1 = {"kiwi", "melon", "mango"}
set2 = {"apple", "cherry"}

set1.update(set2)
print(set1)
#------------------------------
set1 = {"kiwi", "melon", "mango"}
set1.remove("kiwi")
print(set1)
#---------------------------------
set1 = {"kiwi", "mango", "melon"}
set1.clear()
print(set1)
#-------------------------------
set1 = {"kiwi", "melon", "mango"}
set1.pop()
print(set1)
#---------------------------
set1 = {"kiwi", "melon", "mango"}
set1.remove("kiwi")
print(set1)
#---------------------------
set1 = {"kiwi", "mango", "melon"}
set2 = {"apple", "cherry"}

set3 = set1.union(set2)
print(set3)
#----------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)