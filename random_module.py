# Import the random module
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Select a random element from a list
options = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(options)
print(f"Randomly chosen color: {random_color}")

# Generate a list of 5 random numbers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(5)]
print(f"List of 5 random numbers: {random_list}")

# Shuffle a list of elements
random.shuffle(options)
print(f"Shuffled list of colors: {options}")

