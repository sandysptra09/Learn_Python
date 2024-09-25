# track player's inventory
player_inventory = {
    "has_sword": False,
    "gold": 100,
    "solved_puzzle": False
}

# functions to start the game and provide a story introduction to the player
def start_game(show_welcome=True):
    if show_welcome:
        print("Welcome to the Adventure Game!")
        print("You find yourself in a dark forest with two paths ahead.")
        print("One path leads to a mysterious cave, and the other to a quiet village.")
    
    # call function first choice
    first_choice()

# function that give the player the first choice (towards the cave or village)
def first_choice():
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
    print("\nYou arrive at the cave entrance. It's dark inside.")
    print("Before entering the deeper parts of the cave, you notice an ancient stone tablet with a puzzle inscribed on it.")
    if player_inventory["solved_puzzle"]:
        print("You've already solved the puzzle. The path ahead is clear.")
        inside_cave()
    else:
        print("Solve the puzzle to proceed.")
        puzzle()

# A simple puzzle for the player to solve
def puzzle():
    print("\nThe stone tablet reads: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind.'")
    answer = input("What am I? (Type your answer): ").lower()
    
    if answer == "echo":
        print("The puzzle glows, and the path to the cave opens!")
        player_inventory["solved_puzzle"] = True
        inside_cave()
    else:
        print("Wrong answer. The path remains closed.")
        cave()

# function for the story in the cave (after entering the cave)
def inside_cave():
    print("\nInside the cave, you see a treasure chest guarded by a sleeping dragon.")
    print("Do you:")
    print("1. Try to sneak past the dragon to take the treasure")
    print("2. Attack the dragon with your sword")
    print("3. Run away quietly")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        # if the sneak is successful, then the player wins
        print("You sneak past the dragon and open the chest. You found a golden crown!")
        print("Congratulations, you win!")
        
    elif choice == "2":
        # If the player attacks the dragon, check if they have the magic sword
        if player_inventory["has_sword"]:
            print("You charge at the dragon with your magic sword!")
            print("The dragon roars and breathes fire, but your sword deflects the flames.")
            print("You strike the dragon down with your sword. You have defeated the dragon!")
            print("Congratulations, you win!")
        else:
            print("You charge at the dragon with your regular sword, but the dragon wakes up and breathes fire on you.")
            print("You are burned to ashes. Game over.")
        
    elif choice == "3":
        # if the player runs silently, then return to the beginning
        print("You quietly sneak out of the cave and back to the forest.")
        print("Back to the start.")
        
        # start the game again without showing welcome message
        start_game(show_welcome=False)
        
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
        inside_cave()

# function for the story when the player chooses to go to the village
def village():
    print("\nYou arrive at the village. The villagers seem friendly.")
    print("Do you:")
    print("1. Talk to the village elder")
    print("2. Visit the marketplace")
    print("3. Explore the village")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        # if you choose to talk to an elder, proceed to the elder function
        elder()
        
    elif choice == "2":
        # if you select a marketplace, proceed to the marketplace function
        marketplace()

    elif choice == "3":
        explore_village()
        
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
        village()

# function when players talk to village elders
def elder():
    print("\nThe village elder tells you about a hidden treasure in the cave guarded by a dragon.")
    print("Do you:")
    print("1. Go back to the cave to find the treasure")
    print("2. Stay in the village and rest")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # if returning to the cave, call the cave function
        cave()
    elif choice == "2":
        # if the break, the story continues
        print("You rest for the night in the village. In the morning, you feel refreshed and ready for a new adventure!")
        start_game(show_welcome=False)
        
    else:
        print("Invalid choice, please enter 1 or 2.")
        elder()

# function for the story when the player chooses to visit the market
def marketplace():
    print(f"\nYou visit the marketplace. A merchant offers you a magic sword for 100 gold coins. You have {player_inventory['gold']} gold.")
    print("Do you:")
    print("1. Buy the sword")
    print("2. Refuse the offer and leave")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # if you buy a sword, your character becomes stronger
        if player_inventory["gold"] >= 100:
            print("You buy the magic sword and feel much stronger. Maybe now you can defeat the dragon!")
            player_inventory["has_sword"] = True  
            player_inventory["gold"] -= 100
            cave()
        else:
            print("You don't have enough gold! Try exploring or completing tasks to earn more.")
            village()
        
    elif choice == "2":
        # if you decline the offer, move on to another adventure
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

# start the game and start the game from the beginning
start_game()
