x = 5
y = "Jhon"
print(x)
print(y)

# variable names
my_var = "Jhon"
myvar = "Jhon"
_my_var = "Jhon"
myVar = "Jhon"
MYVAR = "Jhon"
myvar2 = "Jhon"
print(my_var)
print(myvar)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Assign Multiple Values
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output variable
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Global Variables

x = "awesome"
def myfunc():
    print("Python is ", x)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is ", x)
myfunc()
print("Python is " + x)


#  Python Variables Code Challenge
x = 5
y = "John"
print(type(x))