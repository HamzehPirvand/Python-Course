f = open("demo.txt")
#--------------------
f = open("demo.txt", "r")
print(f.read())
#-----------------
f = open("E:\demo.txt", "r")
print(f.read())
#-----------------
f = open("demo.txt", "r")
print(f.read(5))
#------------------
f = open("demo.txt", "r")
print(f.readline())
#-----------------------
f = open("demo.txt", "r")
print(f.readline())
print(f.readline())
#----------------------
f = open("demo.txt", "r")
print(f.readline())
f.close()