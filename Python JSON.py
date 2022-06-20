import json

x = '{"name":"John", "age": 30, "city":"new york"}'

y = json.loads(x)

print(y["age"])

#--------------------
import json

x = {
    "name" : "Joe",
    "age" : 30,
    "city" : "New York"
}

y = json.dumps(x)

print(y)