
"""
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1964

}
print(thisdict)

print(thisdict["brand"])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change




# change value
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2020
thisdict.update({"brand": "Chevrolet"})
print(thisdict)

# add item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "white"
thisdict.update({"owner":"Jhon"})
print(thisdict)


# Loop
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# all the keys in the dictionary, one by one
for x in thisdict:
    print(x)

# all the values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])
# 
for x in thisdict.values():
    print(x)

# all the key-value pairs in the dictionary, one by one
for x, y in thisdict.items():
  print(x, y)



# copy a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# mydict = thisdict.copy()
# or
my_dict = dict(thisdict)
print(my_dict)


"""

"""
# Nested dictionaries
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

"""
"""

# 2nd Option
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}


myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
# print(myfamily)

for x, obj in myfamily.items():
  print(x,obj)

#   for y in obj:
#     print(y + ':', obj[y])



x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# use get() mathod
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))



x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' :'green'})
print(x)


"""

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "2024"
}

print(car["model"]) #accessing the value of the key "model"
car.update({"color" : "red"}) #updating the value of the key "color"
print(car) #printing the updated dictionary
car.pop("brand") #removing the key "brand" from the dictionary
print(car) #printing the updated dictionary after removing the key "brand"