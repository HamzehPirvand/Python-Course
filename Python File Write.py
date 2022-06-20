f = open("demo1.txt", "a")
f.write(" now the file has more content")
f.close()

f = open("demo1.txt", "r")
print(f.read())
#------------------------
f = open("demo1.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demo1.txt", "r")
print(f.read())