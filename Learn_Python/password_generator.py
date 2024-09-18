import random
import string

# function to get user preferences
def get_user_preferences():
    while True:
        try:
            # validate the password length
            length = int(input("Enter password length (between 6 and 128): "))
            if length < 6 or length > 128:
                print("Password length must be between 6 and 128. Please try again.")
                continue
        except ValueError:
            print("Please enter a valid number for the password length.")
            continue
        
        # validate input for character types
        use_upper = input("Include uppercase letters? [y/n]: ").lower()
        while use_upper not in ['y', 'n']:
            print("Please enter 'y' for yes or 'n' for no.")
            use_upper = input("Include uppercase letters? [y/n]: ").lower()

        use_lower = input("Include lowercase letters? [y/n]: ").lower()
        while use_lower not in ['y', 'n']:
            print("Please enter 'y' for yes or 'n' for no.")
            use_lower = input("Include lowercase letters? [y/n]: ").lower()

        use_digits = input("Include digits? [y/n]: ").lower()
        while use_digits not in ['y', 'n']:
            print("Please enter 'y' for yes or 'n' for no.")
            use_digits = input("Include digits? [y/n]: ").lower()

        use_symbols = input("Include symbols? [y/n]: ").lower()
        while use_symbols not in ['y', 'n']:
            print("Please enter 'y' for yes or 'n' for no.")
            use_symbols = input("Include symbols? [y/n]: ").lower()

        # ensure at least one character type is selected
        if use_upper == 'n' and use_lower == 'n' and use_digits == 'n' and use_symbols == 'n':
            print("You must select at least one character type for the password. Please try again.")
            continue
        
        return length, use_upper == 'y', use_lower == 'y', use_digits == 'y', use_symbols == 'y'

# function to generate the password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ''
    if use_upper:
        # add uppercase letters A-Z
        char_pool += string.ascii_uppercase  
        
    if use_lower:
        # add lowercase letters a-z
        char_pool += string.ascii_lowercase 
         
    if use_digits:
        # add digits 0-9
        char_pool += string.digits  
        
    if use_symbols:
        # add symbols like @!#%& and more
        char_pool += string.punctuation  
    
    if char_pool == '':
        return "Error: No character types selected."
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    # get user preferences
    length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()

    # generate the password
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    # print the generated password
    print(f"Generated password: {password}")

# execute the main function if this script is run directly.
if __name__ == "__main__":
    main()
