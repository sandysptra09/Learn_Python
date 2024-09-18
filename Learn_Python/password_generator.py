import random
import string

# Function to get user preferences
def get_user_preferences():
    # looping validates preferences
    while True:
        try:
            # validate the password length
            length = int(input("🔐 Enter password length (between 6 and 128): "))
            if length < 6 or length > 128:
                print("🚫 Password length must be between 6 and 128. Please try again.")
                continue
        except ValueError:
            print("⚠️ Please enter a valid number for the password length.")
            continue
        
        # validate input for character types
        use_upper = input("📈 Include uppercase letters? [y/n]: ").lower()
        while use_upper not in ['y', 'n']:
            print("🚫 Please enter 'y' for yes or 'n' for no.")
            use_upper = input("📈 Include uppercase letters? [y/n]: ").lower()
        
        use_lower = input("🔡 Include lowercase letters? [y/n]: ").lower()
        while use_lower not in ['y', 'n']:
            print("🚫 Please enter 'y' for yes or 'n' for no.")
            use_lower = input("🔡 Include lowercase letters? [y/n]: ").lower()

        use_digits = input("🔢 Include digits? [y/n]: ").lower()
        while use_digits not in ['y', 'n']:
            print("🚫 Please enter 'y' for yes or 'n' for no.")
            use_digits = input("🔢 Include digits? [y/n]: ").lower()

        use_symbols = input("🔣 Include symbols? [y/n]: ").lower()
        while use_symbols not in ['y', 'n']:
            print("🚫 Please enter 'y' for yes or 'n' for no.")
            use_symbols = input("🔣 Include symbols? [y/n]: ").lower()

        # ensure at least one character type is selected
        if use_upper == 'n' and use_lower == 'n' and use_digits == 'n' and use_symbols == 'n':
            print("⚠️ You must select at least one character type for the password. Please try again.")
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
        return "🚫 Error: No character types selected."
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# function to save password to file
def save_password(account_name, password):
    with open("passwords.txt", "a") as file:
        file.write(f"Account: {account_name}, Password: {password}\n")
    print("✅ Password saved successfully!")

# function to view saved passwords
def view_saved_passwords():
    try:
        with open("passwords.txt", "r") as file:
            content = file.read()
            if content:
                print("🔎 Saved Passwords:\n", content)
            else:
                print("📜 No passwords saved yet.")
    except FileNotFoundError:
        print("📜 No passwords saved yet.")

# main function
def main():
    print("🎉 Welcome to the Password Manager! 🎉")
    
    while True:
        print("\n🔑 Password Generator Menu:")
        print("1. Generate Password")
        print("2. View Saved Passwords")
        print("3. Exit")
        choice = input("📝 Enter your choice: ")

        if choice == '1':
            length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"✨ Generated password: {password}")
            
            while True:
                save_option = input("💾 Do you want to save this password? [y/n]: ").lower()
                if save_option not in ['y', 'n']:
                    print("🚫 Invalid option. Please enter 'y' for yes or 'n' for no.")
                else:
                    break
            
            if save_option == 'y':
                while True:
                    account_name = input("🔐 Enter the account/site name: ").strip()
                    if not account_name:
                        print("🚫 Account/site name cannot be empty. Please enter a valid name.")
                    else:
                        save_password(account_name, password)
                        break
            elif save_option == 'n':
                print("💬 Password not saved. You can generate a new password or exit the program.")
        elif choice == '2':
            view_saved_passwords()
        elif choice == '3':
            print("👋 Exiting the program. Have a great day!")
            break
        else:
            print("🚫 Invalid choice. Please try again.")

# execute the main function if this script is run directly
if __name__ == "__main__":
    main()
