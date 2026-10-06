
"""

thisset = {"apple", "banana", "cherry","True",1}
print(thisset)
print(type(thisset))

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

"""
"""
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)
print("banana" not in thisset)
print("orange" in thisset)


# add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

"""


"""
# remove item from set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)


# remove random item from set
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

# remove all items from set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# delete set
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)



# Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


thisset = {"apple", "banana", "cherry"}
i = 0
while i < len(thisset):
    print(thisset[i])
    i = i + 1


# Join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set4 = set1 |set2
print(set4)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# intersection of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


"""

colors = {"red", "green", "blue"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(len(colors))