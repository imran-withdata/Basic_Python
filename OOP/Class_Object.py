# class MyClass:
#     x = 5
# # p1 = MyClass()
# # print(p1.x)





# # Multiple Object
# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()

# print(p1.x)
# print(p2.x)
# print(p3.x)


# Use of pass Statement in class
class Person:
    pass

# code challenge

class  Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Jhon", 36)
p1.greet()