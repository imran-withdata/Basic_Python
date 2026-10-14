# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil",36)
# print(p1.name)
# print(p1.age)




# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil",36)
# p2 = Person("Rahim",25)
# p1.name = "Karim"
# print(p2.name)
# print(p1.age)



# class Person:
#     def __init__(self,name , age = 18):
#         self.name = name
#         self.age = age
# p1 = Person("Emil") 
# p2 = Person("Tobis",25)
# print(p1.name, p1.age)
# print(p2.name, p2.age)


# class Person:
#   def __init__(self, name, age, city, country):
#     self.name = name
#     self.age = age
#     self.city = city
#     self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)






# Code Challenge
# Create the Dog class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print(self.name + " says Woof!")

# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
d1.bark()
