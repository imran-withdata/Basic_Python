"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# add items
thistuple = ("apple", "banana", "cherry")
x = list(thistuple)
x.append("Orange")
print(x)
thistuple = tuple(x)
print(thistuple)




fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

"""
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

"""
"""
thistuple = ("apple","banana","cherry")
for x in thistuple:
    print(x)
"""
"""
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
"""
"""
thistuple = ("apple","banana","cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
"""

# Code Challenge

fruits = ("apple","Banana","Cherry")
print(fruits[1])
print(len(fruits))

(a,b,c) = fruits
print(b)