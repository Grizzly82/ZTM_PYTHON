#Create a guessing game where the user has to guess a number between 1 and 100. The program should give hints if the guess is too high or too low, and keep track of the number of attempts.


import random


number = random.randint(1, 100)
attempts = 0
x = True
print("Welcome to the Guessing Game! Try to guess the number between 1 and 100.")
while x:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if attempts == 3:
        print(f"You reached the maximum number of attempts. The correct number was {number}.")
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")    
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
