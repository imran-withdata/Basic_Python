import mymodule
mymodule.greeting("Emil")


import mymodule
a = mymodule.person1["age"]
print(a)


from mymodule import person1
print(person1["age"])


# import platform

# x = dir(platform)
# print(x)

import platform

x = platform.system()
print(x)



import mymodule as mx

a = mx.person1["age"]
print(a)