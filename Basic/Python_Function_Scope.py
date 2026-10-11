# Local scpoe


# def myfunc():
#     x = 300
#     print(x)
# myfunc()

# # Function Inside Functio
# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
# myfunc()



# # Global Scope
# x = 300
# def myfunc():
#     print(x)
# myfunc()
# print(x)



# y = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(y)



# def myfunc():
#     global x 
#     x = 300
# myfunc()
# print(x)



# x = 100

# def myfunc():
#     global x
#     x = 500

# myfunc()
# print(x)





# # Python Decorator
# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner
# @changecase
# def myfunction():
#     return "Hello Sally"
# print(myfunction())





# def changecase (func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello Sally"

# @changecase
# def otherfunction():
#     return "I am speed !"
# print(myfunction())
# print(otherfunction())



# def changecase(func):
#     def myinner(x):
#         return func(x)



# x = lambda a : a + 10
# print(x(5))

# x = lambda a,b : a * b
# print(x(5,6))

# x = lambda a , b, c : a + b +c
# print(x(5,6,2))

# def function(a,b,c):
#     print(a + b + c)
# function(1,2,3)

# def add (a):
#     return a + 10
# add(5)




# def myfunc(n):
#     return lambda a : a * n
# mydoubeler = myfunc(2)
# print(mydoubeler(11))


# def myfunc(n):
#     return lambda a : a*n
# mytripeler = myfunc(3)
# print(mytripeler(5))



# def myfunc(n):
#     return lambda a : a*n
# mytripeler = myfunc(3)
# print(mytripeler(5))


# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x : x%2 != 0 , numbers))
# print(odd_numbers)

# students = [("Emeil", 25), ("Tobias",22), ("Linus", 28)]
# sorted_students = sorted(students, key = lambda x : x[1])
# print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_word = sorted(words, key=lambda x:len(x))
print(sorted_word)