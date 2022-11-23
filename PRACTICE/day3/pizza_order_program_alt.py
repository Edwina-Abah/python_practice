print("Welcome to Python Pizza Deliveries!")
size = input("What size of Pizza do you want? L,S and M?.... ")
add_pepperoni = input("Do you want Pepperoni on it? Y or N.... ")
extra_cheese = input("Do you want an extra_cheese on it? Y or N.... ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese =="Y":
    bill += 1
print(f"Your total bill is ${bill}")