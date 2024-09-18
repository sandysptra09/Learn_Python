import random
import time

# functions to print welcome messages
def welcome_messages(limit_of_guesses):
    # set the border length
    border_length = 50
    
    # print the top border
    print("*" * border_length)
    
    # print a message with a side border
    print("*" + " " * (border_length - 2) + "*")
    print("*" + " " * 10 + "Welcome to the Guess the Number Game!" + " " * 16 + "*")
    print("*" + " " * 10 + "I have chosen a number between 1 and 100." + " " * 18 + "*")
    print("*" + " " * 10 + f"You have {limit_of_guesses} chances to guess." + " " * 30 + "*")
    print("*" + " " * 10 + "Try to guess the number as quickly as possible!" + " " * 6 + "*")
    
    # print the bottom border
    print("*" + " " * (border_length - 2) + "*")
    print("*" * border_length)
    
# function input user name
def get_user_name():
    """Get the user's name."""
    return input("Enter your name: ").strip()

# function to print the instructions
def instructions():
    """Print the instructions on how to play the game."""
    print('''\n
    Instructions:
    1. I will choose a random number between 1 and 100.
    2. Your goal is to guess the number I have chosen.
    3. You have a limited number of chances (10) to guess the correct number.
    4. If your guess is too low, I will tell you that it's too low.
    5. If your guess is too high, I will tell you that it's too high.
    6. If you guess the correct number, you win!
    7. If you run out of chances, I will reveal the correct number.
    8. You can choose to play again after the game ends.
    ''')

# function to confirm if the user is ready
def confirm_readiness():
    """Ask the user if they are ready to start the game."""
    while True:
        response = input("Are you ready to start? (yes/no): ").lower()
        if response == 'yes':
            break
        elif response == 'no':
            print(f"Okay, take your time. You can start when you're ready.")
        else:
            print("Please enter 'yes' or 'no'.")

# function for guessing the number of chances
def guess_the_number():
    # Determine the number range
    secret_number = random.randint(1, 100)
    guess = None
    number_of_guesses = 0
    limit_of_guesses = 10
    guessed_numbers = []
    
    # start timers
    start_time = time.time()
    
    # show welcome message
    welcome_messages(limit_of_guesses)
    
    # show input name
    user_name = get_user_name()
    
    # confirm readiness
    confirm_readiness()
    
    # show instructions
    instructions()
    
    # logic game
    while guess != secret_number and number_of_guesses < limit_of_guesses:
        try:
            guess = int(input("Enter your guess: "))
            number_of_guesses += 1
            
            if guess in guessed_numbers:
                print("You've already guessed that number. Try a different number.")
                number_of_guesses -= 1
                continue
            
            guessed_numbers.append(guess)
            
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                end_time = time.time()  # End timer
                elapsed_time = round(end_time - start_time, 2)
                print(f"Congratulations {user_name}! You guessed the correct number in {number_of_guesses} guesses and {elapsed_time} seconds!")
                break
        except ValueError:
            print("Enter a valid number.")
    
    if guess != secret_number:
        print(f"What a shame {user_name}! You've run out of chances. The correct number was {secret_number}.")
    
    # offering a replay
    play_again = input("Want to play again? [yes/no]: ").lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thank you for playing!")

# start the game
guess_the_number()
