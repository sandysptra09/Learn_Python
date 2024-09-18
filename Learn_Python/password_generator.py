import random
import string

# function get input from user
def get_user_preferences():
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? [y/n]: ").lower() == 'y'
    use_lower = input("Include lowercase letters? [y/n]: ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? [y/n]: ").lower() == 'y'
    
    return length, use_upper, use_lower, use_digits, use_symbols

# function generate password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ''
    if use_upper:
        # A-Z
        char_pool += string.ascii_uppercase  
        
    if use_lower:
        # a-z
        char_pool += string.ascii_lowercase 
         
    if use_digits:
        # 0-9
        char_pool += string.digits  
        
    if use_symbols:
        # @!#%&...
        char_pool += string.punctuation  
    
    if char_pool == '':
        return "Error: No character types selected."
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()