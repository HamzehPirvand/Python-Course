import datetime

x = datetime.datetime.now()
print(x)
#--------------
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#--------------------
import datetime

x = datetime.datetime(2021, 9, 8)

print(x)
#----------------------
import datetime

x = datetime.datetime(2018, 6, 18)
print(x.strftime("%B"))