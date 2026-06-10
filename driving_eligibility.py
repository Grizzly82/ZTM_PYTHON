from datetime import datetime

today = datetime.now()
current_year = today.year

birth_year = input("Enter your birth year: ")
age = current_year - int(birth_year)
print(f"You are {age} years old.")

# Check if eligible to drive (minimum age is 16)
if age >= 16:
    print("You are old enough to drive!")
else:
    years_until_eligible = 16 - age
    print(f"You are not old enough to drive yet. You will be eligible in {years_until_eligible} years.")
