#Nested Conditinal Statement with elif
print("Welcome to the rollercoster")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You are qualified to ride on the rollercoster")
    age = int(input("How Old are you? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
            print("please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")