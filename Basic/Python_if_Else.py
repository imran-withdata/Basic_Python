

# a = 30
# b = 200
# if b>a:
#     print("b is greather than a")


# number = 15
# if number>0:
#     print("The number is Positive")



# age = 20
# if age >= 18:
#   print("You are an adult")
#   print("You can vote")
#   print("You have full legal rights")



# a = 33
# b = 33
# if b > a :
#     print("b is grater then a")
# elif a == b:
#     print("a and b equal")



# score = 75

# if score >= 90:
#     print("Gread : A")
# elif score >= 80:
#     print("Gread : B")
# elif score >= 70:
#     print("Gread : C")
# elif score >= 60:
#     print("Gread : D")

    




# day = 3

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7 :
#     print("Sunday")





# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")


# number = 7
# if number % 2 == 0:
#     print("The number is even")
# else : 
#     print("The number is odd")


# temperature = 9

# if temperature > 30:
#     print("It's hot outside!")
# elif temperature > 20:
#     print("It' s warm outside!")
# elif temperature > 10 :
#     print("It's cool outside!")
# else:
#     print("It's cold outside!")



# username = "Emil"
# if len(username) > 0:
#     print(f"Welcome, {username} !")
# else:
#     print("Error: Username cannot be empty")


# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print("Both conditions are True")
# if a > b or a > c:
#     print("At least one of the conditions is True")  

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")


# Logical operator
# age = 25
# is_student = False
# has_discount_code = True

# if ( age < 18 or age > 65 )and not is_student or has_discount_code:
#     print("Discount applies!")


# temperature = 25
# is_raining = False
# is_weekend = True
# if (temperature > 20 and not is_raining) or is_weekend:
#     print("Great day for outdoor activities!")




# username = "Tobias"
# password = "secret123"
# is_verified = True

# if username and password and is_verified:
#   print("Login successful")
# else:
#   print("Login failed")





# Nested If

# score = 85
# attendance = 90
# submitted = False

# if score >= 60:
#   if attendance >= 80:
#     if submitted:
#       print("Pass with good standing")
#     else:
#       print("Pass but missing assignment")
#   else:
#     print("Pass but low attendance")
# else:
#   print("fail")


# x = 41
# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else :
#         print("but not above 20.")
# else :
#     print("less 40")






# age = 25
# has_license = True
# if age >= 18:
#     if has_license:
#         print("You can drive")
#     else:
#         print("You need License.")
# else:
#     print("You are too young to drive")




# temperature = 25
# is_sunny = True
# if temperature > 20:
#     if is_sunny:
#         print("Perfect beach weather!") 


# temperature = 25
# is_sunny = True
# if temperature > 20 and is_sunny:
#     print("Perfect beach weather!")



# # Nested If


# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")



# pass Statement

# age = 20

# if age < 18:
#   pass # TODO: Add underage logic later
# else:
#   print("Access granted")


# This works correctly with pass

# score = 85

# if score > 90:
#   pass # This is excellent
# print("Score processed")


# value = 50
# if value < 0 :
#     print("Negative Value")
# elif value == 0:
#     pass #Zero case - no action needed
# else :
#     print("Positive value")


# def calculate_discount(price):
#   pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet



age = 20
if age <= 13:
    print("Child")
elif age <= 18:
    print("Teenager")
else:
    print("Adult") 