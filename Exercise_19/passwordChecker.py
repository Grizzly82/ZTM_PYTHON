#password checker 
#at least 8 characters long
#Alphabetic characters (both uppercase and lowercase)
#At least one numeric digit
#At least one special character (e.g., !, @, #, $, etc.)

def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one numeric digit."
    
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."
    
    return "Password is strong."

# Example usage
password = input("Enter a password to check its strength: ")
strength_message = check_password_strength(password)
print(strength_message)