from datetime import datetime

today = datetime.now()
current_year = today.year

birth_year = input("Enter your birth year: ")
age = current_year - int(birth_year)
#print("You are", age, "years old.")
print(f"You are {age} years old.")
# The above code takes the user's birth year as input, converts it to an integer, and calculates the age by subtracting the birth year from the current year. Finally, it prints the age to the user.
# Note: The input() function returns a string, so we need to convert it to an integer using int() before performing the subtraction.
# Example usage:
# Enter your birth year: 1990
# You are 34 years old.
