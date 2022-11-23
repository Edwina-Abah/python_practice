#Treasure is land quest game.
print("Welcome to Treasure Island\nYour mission is to find the treasure.")

cross_road = input("You are on a cross road, where do you go?. left or right ")
cross_road = cross_road.lower()
if cross_road == 'right':
    wait = input("You have come to the lake. There is an Island at the middle of the lake.Type 'wait' to wait for a bot. Type 'swim' to swim across. ")
    wait = wait.lower()
    if wait == 'wait':
        blue = input("You have arrived at the Island unharmed. There is a house with 3 doors. One Red, One Blue, One Green. Which colour do you choose?")
        blue = blue.lower()
        if blue == 'blue':
            print("Congratulations")
else:
    print("Game Over")