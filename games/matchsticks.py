match_sticks = 21

player_name = input("Please enter your name: ")
print("Welcome " + str(player_name) + " to the 21 match sticks game...")

while (match_sticks > 0):
    num_picked = int(input(player_name + ", pick either 1,2,3 or 4 match sticks: "))
    print("You picked " + str(num_picked) + " match sticks.")

    match_sticks = match_sticks - num_picked
    if(match_sticks == 1):
        print("I have to pick the last match stick. I loose.")
        break

    match_sticks = match_sticks - (5 - num_picked)
    print("I picked " + str(5 - num_picked) + ' match sticks.')

    print("Number of match sticks remaining is " + str(match_sticks))
    
    if(match_sticks == 1):
        print(player_name + ", You have to pick the last match stick. You loose.")
        break
