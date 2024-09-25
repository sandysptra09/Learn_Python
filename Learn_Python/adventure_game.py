# functions to start the game and provide a story introduction to the player
def start_game():
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
    print("Do you:")
    print("1. Enter the cave")
    print("2. Run away back to the forest")
    
    # input player options
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # if you choose to enter the cave, proceed to the inside_cave function
        inside_cave()
        
    elif choice == "2":
        # narration when players run and fall then end of story
        print("You run back to the forest, but you trip and fall into a pit!")
        print("Game over.")
        
    else:
        print("Invalid choice, please enter 1 or 2.")
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
        # if you attack the dragon, then the player fails and the story ends
        print("You charge at the dragon with your sword, but the dragon wakes up and breathes fire on you.")
        print("You are burned to ashes. Game over.")
        
    elif choice == "3":
        # if the player runs silently, then return to the beginning
        print("You quietly sneak out of the cave and back to the forest.")
        print("Back to the start.")
        
        # start the game again
        start_game()
        
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
        inside_cave()

# function for the story when the player chooses to go to the village
def village():
    print("\nYou arrive at the village. The villagers seem friendly.")
    print("Do you:")
    print("1. Talk to the village elder")
    print("2. Visit the marketplace")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # if you choose to talk to an elder, proceed to the elder function
        elder()
        
    elif choice == "2":
        # if you select a marketplace, proceed to the marketplace function
        marketplace()
        
    else:
        print("Invalid choice, please enter 1 or 2.")
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
        start_game()
        
    else:
        print("Invalid choice, please enter 1 or 2.")
        elder()

# function for the story when the player chooses to visit the market
def marketplace():
    print("\nYou visit the marketplace. A merchant offers you a magic sword for 100 gold coins.")
    print("Do you:")
    print("1. Buy the sword")
    print("2. Refuse the offer and leave")
    choice = input("Enter 1 or 2:")

    if choice == "1":
        # if you buy a sword, your character becomes stronger
        print("You buy the magic sword and feel much stronger. Maybe now you can defeat the dragon!")
        # continue to the cave with a sword
        cave()
        
    elif choice == "2":
        # if you decline the offer, move on to another adventure
        print("You leave the marketplace and continue your adventure.")
        start_game()
    else:
        print("Invalid choice, please enter 1 or 2.")
        marketplace()

# Start the game and start the game from the beginning
start_game()
