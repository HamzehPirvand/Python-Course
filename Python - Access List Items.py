list1 = ["apple", "banana", "kiwi"]
print(list1[1])
#------------------
list1 = ["apple", "banana", "kiwi"]
print(list1[-1])
#---------------------
thislist = ["apple", "bnana", "kiwi", "orange", "cherry", "melon", "mango"]
print(thislist[2:5])
#------------------------
thislist = ["apple", "bnana", "kiwi", "orange", "cherry", "melon", "mango"]
print(thislist[:4])
#-----------------
thislist = ["apple", "bnana", "kiwi", "orange", "cherry", "melon", "mango"]
print(thislist[2:])
#----------------------
thislist = ["apple", "bnana", "kiwi", "orange", "cherry", "melon", "mango"]
print(thislist[-4:-2])
#-------------------------
thislist = ["apple", "bnana", "kiwi", "orange", "cherry", "melon", "mango"]
if "apple" in thislist:
    print("Yes, apple is in thislist")