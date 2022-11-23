#LOVE CALCULATOR CHALLENGE DAY 4
print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")                                                  #input functions
name2 = input("What is your partner name?\n")

name = name1 + name2                                                                   #concatinate variable
name = name.lower()                                                                    #covert inputed uppercase into lovercase in a variable
                                                                                       
import re
true = (len(re.findall('[true]',name)))                                               #multiple count statement
love = (len(re.findall('[love]',name)))

true_love = int(f"{true}{love}")                                                      #concatinate string and convert to integer

if true_love < 10 or true_love > 90:                                                  #conditional statement with operators
    print(f"Your love percentage is {true_love}%\nYou are like Coke and Mentos")
elif true_love >= 40 and true_love <= 50:                                             #conditional statement with operators
    print(f"Your love percentage is {true_love}%\nYou are good together")
else:
    print(f"Your love percentage is {true_love}%\nGo and find your true love")



                    