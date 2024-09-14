import random
import time

# list welcome message
welcome_messages = [
    'WELCOME TO SANSAN GAMES!',
    'ARE YOU READY TO FIND SANPY?',
    'SANPY IS HIDING, LET\'S GO!',
    'LET THE HUNT FOR SANPY BEGIN!'
]

# welcome messages displayed in sequence
print("*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*")
for message in welcome_messages:
    print(f"*****    {message}")
print("*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*")

# input name of user
user_name = input("Enter your name : ")

# provide instructions on how to play
print(f'''
Hello {user_name}!

Welcome to the game where you need to find SANPY hidden in one of the caves. Here's how to play:

1. You will choose a difficulty level: easy (4 caves), medium (6 caves), or hard (8 caves).
2. SANPY is hiding in one of the caves. You have to guess which cave SANPY is in.
3. You have 3 attempts to guess the right cave.
4. If you guess correctly, you win! If not, SANPY's location will be revealed after you run out of attempts.
5. You can choose to play again after each game.

Good luck and have fun!

''')

# choose difficulty
difficulty = input("Choose difficulty: easy (4 caves), medium (6 caves), hard (8 caves): ").lower()

if difficulty == 'easy':
    num_caves = 4
    
    # 30 seconds for easy
    time_limit = 30  
    
elif difficulty == 'medium':
    num_caves = 6
    
    # 45 seconds for medium
    time_limit = 45  
    
elif difficulty == 'hard':
    num_caves = 8
    
    # 60 seconds for hard
    time_limit = 60  
    
else:
    print("Invalid choice, defaulting to easy.")
    num_caves = 4
    time_limit = 30

print(f'\nYou have chosen {difficulty} difficulty with {num_caves} caves and {time_limit} seconds time limit!')
print("Check out the cave below")
print(" | ".join(["_" for _ in range(num_caves)]))

def display_caves(num_caves, sanpy_pos=None, user_guess=None):
    
    """Display a more detailed visualization of the caves."""
    caves = ['_' for _ in range(num_caves)]  
    
    if user_guess is not None:
        # mark the user's guess
        caves[user_guess - 1] = 'X'  
    if sanpy_pos is not None:
         # mark SANPY's position
        caves[sanpy_pos - 1] = 'S' 

    if num_caves == 4:
        print(f"""
  ____  ____ 
 |_{caves[0]}__||_{caves[1]}__|
 |____||____|
 |_{caves[2]}__||_{caves[3]}__|
 |____||____|
""")
    elif num_caves == 6:
        print(f"""
  ____  ____  ____ 
 |_{caves[0]}__||_{caves[1]}__||_{caves[2]}__|
 |____||____||____|
 |_{caves[3]}__||_{caves[4]}__||_{caves[5]}__|
 |____||____||____|
""")
    elif num_caves == 8:
        print(f"""
  ____  ____  ____  ____ 
 |_{caves[0]}__||_{caves[1]}__||_{caves[2]}__||_{caves[3]}__|
 |____||____||____||____|
 |_{caves[4]}__||_{caves[5]}__||_{caves[6]}__||_{caves[7]}__|
 |____||____||____||____|
""")


# initialize score
score = 0

# main game loop
while True:
    
    # reset SANPY's position for a new game
    sanpy_position = random.randint(1, num_caves)  
    
    print("SANPY is hiding in one of these caves:")
    
    # display empty caves before the game starts
    display_caves(num_caves)  
    
    attempts = 3
    
    # start the timer
    start_time = time.time()  
    
    while attempts > 0:
        try:
            elapsed_time = time.time() - start_time
            remaining_time = max(0, int(time_limit - elapsed_time))
            
            if remaining_time == 0:
                print("Time's up! You ran out of time.")
                print(f"SANPY was in cave {sanpy_position}. Better luck next time!")
                break
            
            user_choice = int(input(f"Which cave do you think SANPY is in? You have {attempts} attempts left and {remaining_time} seconds left [1 / {num_caves}] : "))
            if user_choice not in range(1, num_caves + 1):
                print(f"Please choose a number between 1 and {num_caves}.")
                continue
            
            # show user's guess
            display_caves(num_caves, user_guess=user_choice)  
            
            if user_choice == sanpy_position:
                print(f"Congratulations {user_name}, you found SANPY!")
                score += 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong guess! You have {attempts} attempts left.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == 0 and remaining_time > 0:
        print(f"Sorry {user_name}, you're out of attempts! SANPY was in cave {sanpy_position}. Better luck next time!")
    
    # show the correct position of SANPY after the game ends
    print(f"SANPY was in cave {sanpy_position}. Here's the correct map:")
    display_caves(num_caves, sanpy_pos=sanpy_position)  
    
    # display score
    print(f"Your current score is: {score}")
    
    # replay the game
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
