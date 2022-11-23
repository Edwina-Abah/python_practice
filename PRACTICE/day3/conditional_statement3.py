#Nested Conditinal Statement
print("Welcome to the rollercoster")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You are qualified to ride on the rollercoster")
    age = int(input("How Old are you? "))
    if age >= 18:
        print("Please pay $12")
    else:
        print("Please pay $7")
else:
    print("Sorry, you have to grow taller before you can ride")