def my_function():
  print("Hello from a function")
my_function()
my_function()


# Without functions - repetitive code: example

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)







# With functions - reusable code:

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celcius(77))
print(fahrenheit_to_celcius(95))
print(fahrenheit_to_celcius(50))
print(fahrenheit_to_celcius(55))


# Return Value
def get_greeting():
    return "Hello from a function"

massage = get_greeting()
print(massage)

tit = get_greeting()
print(tit)


# I  can use the returned value directly:
def get_greeting():
    return "Hello from a function"
print(get_greeting())


def my_function():
  pass









# python arguments
def my_function(fname):
    print(fname + "Refnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




def my_function(fname):
    print(fname + " Rahman")

my_function("Imran")
my_function("Kalam")
my_function("Yeasin")


def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument




# 2 arguments
def my_function(fname , lname):
    print(fname + " " + lname)
my_function("Emil","Refnes")



def my_function(name = "Friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


def my_function( country = "Norway"):
    print("I am from ", country)
my_function("Sweden")
my_function("Japan")
my_function()
my_function("Brazil")




def my_function(animal, name):
    print("I have a ", animal)
    print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")


def my_function (animal, name):
    print("I have a ", animal)
    print("My", animal + "'s name is", name)
my_function("dog","Buddy")



def my_function (animal , name , age):
    print("I have a", age, "year old ", animal, "named", name)
my_function("dog" , name = "Buddy", age = 5)


def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple","banana","cherry"]
my_function(my_fruits)


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age" : 25}
my_function(my_person)



def my_function (x , y):
    return x + y
result = my_function(5 , 3)
print(result)



# A function that returns a list:

def my_function ():
    return ["apple","banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])


# A function that returns a tuple:
def my_function ():
    return (10 , 20)
x,y = my_function()
print("X", x)
print("Y", y)











# *args and **kwargs


def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



def my_function(**kwargs):
    print(kwargs)

my_function(name = "Imran", age = 25)



def my_function(*dict):
    print(dict)

my_function(name = "Imran", age = 25)




def my_function(*args):
    print("type:", type(args))
    print("First argument :", args[0])
    print("First argument :", args[1])
    print("All arguments:", args)
my_function("Emil","Tobias","Linus")




# Using *args with Regular Arguments
def my_function(greeting, *names):
    for name in names:
        print(greeting,name)
my_function("Hello","Emil","Tobias","Linus")



def my_function(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
print(my_function(1,2,3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_function (*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(my_function(3,7,2,9,1))


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**myvar):
    print("Type:",type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data", myvar)
my_function(name = "Tobias", age = 25, city = "Bergen")


def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key,value in details.items():
        print("",key + ":", value)
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


def my_function(title,*args , **kwargs):
    print("Title:", title)
    print("positional arguments:", args)
    print("Keyword Arguments:", kwargs)
    # for key, value in kwargs.items():
    #     print("",key + ":", value)

my_function("User Info","Emil","Tobias", age =25,city="Oslo")


def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)


def my_function(fname,lname):
    print("Hello", fname,lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)   # my_function(fname="Emil", lname="Refsnes")