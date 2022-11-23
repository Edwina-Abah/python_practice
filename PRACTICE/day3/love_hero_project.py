#Love Hero game------by Prosper Agada 05-11-2022
print("Your are Welcome to LOVE HERO\nDiscover how much you love your partner by the end of this game")
me = input("What is your name?.... ")
lover = input("What is your partner name?.... ")
print(f"LEVEL ONE \n You just received a phone call from your best friend james..\nplease help! {lover} your lover had just been kidnapped by some armed men")
Map = input("What will you do?.....\na)call the corps\nb)find a map\nc)call her parents\n.... ")
if Map == 'b':
    print(f"Nice Job")
    river = input(f"You just discovered the location where {lover} was held hostage\nest-virginia\nIn a Tower at the middle of a lake\n'KURI'\n ooh the lake is big!..\nWhat will you do?\na)wait for a boat\nb)find a bridge\nc)swim to the next end\n....")
    if river == 'a':
        print("Very good\nAli the fisherman offered you a ride")
        men = input(f"Ooh my!\ni can see some armed guard at the entrance of the tower\nYou need a weapon\nto get a weopon you must solve Ali riddle\nAre you ready!....Y/N\n....")
        if men == "Y":
            riddle = input("As i was going to st.lves, i meet a man with seven wives.\nEvery wife had seven sacks\nEvery sack had seven cats\nEvery cat had seven kittens\nKittens,Cats,Sacks and Wives\nHow many going to st.ives\na)5\nb)1\nc)28\n....")
            #if riddle == "b":
                

