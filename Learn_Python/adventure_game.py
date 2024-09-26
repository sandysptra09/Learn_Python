# track player's inventory
player_inventory = {
    "has_sword": False,
    "has_shield": False,
    "has_magic_key": False,
    "gold": 100,
    "solved_cave_puzzle": False,
    "solved_village_puzzle": False,
    "found_hidden_treasure": False,
    "dragon_health": 100
}

# functions to start the game and provide a story introduction to the player
def start_game(show_welcome=True):
    
    # display a welcome message if show_welcome True
    if show_welcome:
        print("Welcome to the Expanded Adventure Game!")
        print("You find yourself in a dark forest with two paths ahead.")
        print("One path leads to a mysterious cave, and the other to a quiet village.")
    
    # direct players to make the first choice
    first_choice()

# function that gives the player the first choice (towards the cave or village)
def first_choice():
    
    # giving the first two options to players
    print("\nDo you:")
    print("1. Walk towards the cave")
    print("2. Head to the village")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # if the player chooses 1, enter the cave
        cave()
        
    elif choice == "2":
        
        # if the player chooses 2, go to the village
        village()
        
    else:
        print("Invalid choice, please enter 1 or 2.")
        first_choice()

# functions for the story when the player chooses to go to the cave
def cave():
    
    # start a story in the cave
    print("\nYou arrive at the cave entrance. It's dark inside.")
    print("Before entering the deeper parts of the cave, you notice an ancient stone tablet with a puzzle inscribed on it.")
    
    # if the cave riddle is solved
    if player_inventory["solved_cave_puzzle"]:
        print("You've already solved the puzzle. The path ahead is clear.")
        
        # continue into the cave
        inside_cave()
        
    else:
        print("Solve the puzzle to proceed.")
        
        # show cave puzzle
        cave_puzzle()

# a more complex puzzle for the player to solve in the cave
def cave_puzzle():
    
    # show puzzles to players
    print("\nThe stone tablet reads: 'I’m tall when I’m young, and I’m short when I’m old. What am I?'")
    answer = input("What am I? (Type your answer): ").lower()
    
    # if the answer is correct, open the way to the cave
    if answer == "candle":
        print("The puzzle glows, and the path to the cave opens!")
        
        # mark the puzzle as solved
        player_inventory["solved_cave_puzzle"] = True
        
        # continue into the cave
        inside_cave()
        
    else:
        # wrong answer, player must try again
        print("Wrong answer. The path remains closed.")
        cave()

# function for the story in the cave (after entering the cave)
def inside_cave():
    # start a story while in the cave
    print("\nInside the cave, you see a treasure chest guarded by a sleeping dragon.")
    print("Do you:")
    print("1. Try to sneak past the dragon to take the treasure")
    print("2. Attack the dragon with your sword")
    print("3. Run away quietly")
    choice = input("Enter 1, 2, or 3: ")

    # players try to sneak up on the treasure
    if choice == "1":
        print("You sneak past the dragon and open the chest. You found a golden crown and a magic key!")
        
        # players get the magic key
        player_inventory["has_magic_key"] = True
        
        # players find treasure
        player_inventory["found_hidden_treasure"] = True
        
        # players win
        print("Congratulations, you win!")
        
    elif choice == "2":
        # players choose to fight with dragons
        fight_dragon()
        
    elif choice == "3":
        # players escape from the cave
        print("You quietly sneak out of the cave and back to the forest.")
        
        # return to the beginning of the game
        start_game(show_welcome=False)
        
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
        inside_cave()

# function to fight the dragon with more complexity
def fight_dragon():
    # players start a battle with a dragon
    print("\nYou engage in a battle with the dragon!")
    
    # players use a sword
    if player_inventory["has_sword"]:
        print("You use your sword to strike the dragon.")
        
        # reduce dragon health
        player_inventory["dragon_health"] -= 50
        if player_inventory["dragon_health"] <= 0:
            # if the dragon loses, the player wins
            print("You have defeated the dragon! You open the treasure chest and find a golden crown and a magic key!")
            player_inventory["has_magic_key"] = True
            player_inventory["found_hidden_treasure"] = True
            print("Congratulations, you win!")
        else:
            
            # dragon counterattacks
            print("The dragon is still alive and breathes fire at you. You need a shield to block the flames!")
            
            # players have a shield
            if player_inventory["has_shield"]:
                print("You use your shield to block the flames and strike the dragon again!")
                # second attack
                player_inventory["dragon_health"] -= 50
                if player_inventory["dragon_health"] <= 0:
                    print("You have defeated the dragon and won!")
                else:
                    print("The dragon is too strong! You run away.")
                    start_game(show_welcome=False)
            else:
                
                # player has no shield, loses
                print("You don’t have a shield. The dragon burns you to ashes. Game over.")
    else:
        # player has no sword, loses
        print("You don’t have a sword. The dragon wakes up and breathes fire. Game over.")

# function for the story when the player chooses to go to the village
def village():
    # start a story in the village
    print("\nYou arrive at the village. The villagers seem friendly.")
    print("Do you:")
    print("1. Talk to the village elder")
    print("2. Visit the marketplace")
    print("3. Explore the village")
    choice = input("Enter 1, 2, or 3: ")

    # players choose to talk to village elders
    if choice == "1":
        elder()
        
    elif choice == "2":
        # players choose to visit the marketplace
        marketplace()
        
    elif choice == "3":
        # players explore the village
        explore_village()
        
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
        village()

# function when players talk to village elders
def elder():
    # stories when talking to village elders
    print("\nThe village elder tells you about a hidden treasure in the cave guarded by a dragon.")
    print("The elder also gives you a riddle: 'The more of this there is, the less you see. What is it?'")
    answer = input("What is it? (Type your answer): ").lower()

    # correct answer, player gets a shield
    if answer == "darkness":
        print("Correct! The elder gives you a shield as a reward. This will help you in your fight against the dragon!")
        # player gets a shield
        player_inventory["has_shield"] = True
        print("Do you:")
        print("1. Go back to the cave to find the treasure")
        print("2. Stay in the village and rest")
        choice = input("Enter 1 or 2: ")

        # players return to the cave
        if choice == "1":
            cave()
        elif choice == "2":
            print("You rest for the night in the village. In the morning, you feel refreshed and ready for a new adventure!")
            start_game(show_welcome=False)
        else:
            print("Invalid choice, please enter 1 or 2.")
            elder()
    else:
        print("Wrong answer. The elder refuses to help you.")
        village()

# function for the story when the player chooses to visit the market
def marketplace():
    # players visit the market and can buy magic swords
    print(f"\nYou visit the marketplace. A merchant offers you a magic sword for 100 gold coins. You have {player_inventory['gold']} gold.")
    print("Do you:")
    print("1. Buy the sword")
    print("2. Refuse the offer and leave")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        if player_inventory["gold"] >= 100:
            
            # player enough gold, buy a sword
            print("You buy the magic sword and feel much stronger. Maybe now you can defeat the dragon!")
            player_inventory["has_sword"] = True  
            # reduce gold
            player_inventory["gold"] -= 100
            cave()
        else:
            print("You don't have enough gold! Try exploring or completing tasks to earn more.")
            village()
    elif choice == "2":
        # players choose to leave the market
        print("You leave the marketplace and continue your adventure.")
        start_game(show_welcome=False)
        
    else:
        print("Invalid choice, please enter 1 or 2.")
        marketplace()

# function to explore the village
def explore_village():
    print("\nYou explore the village and find a small pond with shimmering water. You also meet other villagers who talk about hidden gold in the forest.")
    print("Do you want to:")
    print("1. Search for the hidden gold in the forest")
    print("2. Return to the village center")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("You explore the forest and find 50 gold coins hidden under a tree!")
        player_inventory["gold"] += 50
        print(f"You now have {player_inventory['gold']} gold.")
        village()
    elif choice == "2":
        village()
    else:
        print("Invalid choice, please enter 1 or 2.")
        explore_village()

# start the game
start_game()
