# print("Hello, World!")
# name = input("What is your name?")
# print(name)

fname = input("What is your first name?")
lname = input("What is your last name?")
print( fname + lname)
# Slicing
#Count the positions of letters

ballparkearnings = "1,201,411"
money = ballparkearnings[2:9]
print(money)

#You can also slice a string by just using the number position followed by : if u want remaining part of string
#Using number: will print whatever position and remaining

food = "I am hungry, I am not hungry"
print(food[12:])

#Using :number will print to whatever position is called and stops
food1 = "Hotdogs, Hamburgers"
print(food1[:7])