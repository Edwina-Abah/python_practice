#Adding a logical operator using and.
print("Welcome to the rollercoster")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You are qualified to ride on the rollercoster")
    age = int(input("How Old are you? "))
    if age < 12:
        print("children ticket are $5")
        bill = 5
    elif age <= 18:
        print("youth ticket $7")
        bill = 7
    elif age >= 45 and age <= 50:
        print("You don't have to pay for the ticket")
    else:
        print("adult tickt $12")
        bill = 12
    photo_shot = input("Do you want a photo? (Y orN) ")
    if photo_shot == 'Y':
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")