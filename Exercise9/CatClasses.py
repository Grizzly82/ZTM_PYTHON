# Exercise Cats Everywhere
# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
#SCROLL FOR ANSWERS

# 1 Instantiate the Cat object with 3 cats.
kitty1 = Cat("Whiskers", 5)
kitty2 = Cat("Mittens", 3)
kitty3 = Cat("Shadow", 7)

# 2 Create a function that finds the oldest cat.
def find_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
oldest_cat = find_oldest_cat(kitty1, kitty2, kitty3)
print(f"The oldest cat is {oldest_cat.age} years old.")
