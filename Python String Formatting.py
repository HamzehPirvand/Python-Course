price = 49
txt = "the price is {} dollars"
print(txt.format(price))
#-----------------------------
name = "Sarah"
txt = "her name is {}"
print(txt.format(name))
#------------------------
price = 50
txt = "the price is {:.2f} dollars"
print(txt.format(price))
#---------------------
quantity = 3
itemno = 567
price = 50

myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity,itemno,price))
#------------------------------
name = "Joe"
family = "Olsan"
year = 25

x = "my first name is {} and my last name is {} and I am {} years old"
print(x.format(name,family,year))
