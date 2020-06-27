match_sticks = 21

player_name = input("Please enter your name: ")
print("Welcome " + str(player_name) + " to the 21 match sticks game...")

while (True):
    # Player 1 input...
    num_picked = int(input(player_name + ", pick either 1,2,3 or 4 match sticks: "))
    print("You picked " + str(num_picked) + " match sticks.")

    #validating the rule 1...
    if num_picked <= 0 or num_picked >= 5:
        print(player_name + ", please dont cheat.")
        continue
    
    match_sticks = match_sticks - num_picked
    print("Number of match sticks remaining is " + str(match_sticks))    
    
    if(match_sticks == 1):
        print("I have to pick the last match stick. I loose.")
        break
    
    num_computer_pick = 5 - num_picked
    match_sticks = match_sticks - num_computer_pick
    print("I picked " + str(num_computer_pick) + ' match sticks.')

    print("Number of match sticks remaining is " + str(match_sticks))
    
    if(match_sticks == 1):
        print(player_name + ", You have to pick the last match stick. You loose.")
        break

print("Game over...")