x = range(3,10)
print(x)
for i in x :
    print(i)




# call the range with 3 argument
x = range(3, 10, 2)

for i in range(10):
    print(i)

print(list(range(5)))
print(list(range(1,6)))
print(list(range(5,20,3)))


# range Slicing
r = range(10)
print(r[2])
print(r[:3])



# Membership Testing
r = range(0,10,2)
for i in r:
    print(i)
print(6 in r)
print(7 in r)



# Length checking
r = range(0,10,2)
print(len(r))

