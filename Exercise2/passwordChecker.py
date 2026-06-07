user_name = input("Enter your username: ")
password = input("Enter your password: ")

masked_password = '*' * len(password)
print(f"Username: {user_name}")
print(f"Password: {masked_password}")
# The above code prompts the user to enter a username and password. It then masks the password by replacing each character with an asterisk (*) and prints the username and the masked password to the user. This is a common practice to protect the user's password from being displayed in plain text.
# Example usage:
# Enter your username: john_doe
# Enter your password: mysecretpassword
# Username: john_doe
# Password: *****************