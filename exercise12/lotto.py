# QUESTION 3

# Write a Python script called lotto.py that will generate and display 6 unique random lottery numbers between 1 and 50
# Think about which Python data structure is best suited to store the numbers
# Use the Python help() function to find out which function to use from the Python standard library called random

# import random
# help(random)

from random import randint

lotto_generator = input("Press 'y' to create 6 random lottery numbers (1-50), or any other key to exit: ")

while lotto_generator.lower() == "y":

    # Created a set to hold the numbers as sets are mutable and unique, so any duplicate numbers will be removed
    lotto_numbers = set()
    while len(lotto_numbers) < 6:
        lotto_numbers.add(randint(1, 50))

    final_numbers = sorted(lotto_numbers)

    print("Your random numbers are: " + ", ".join(str(num) for num in final_numbers))

    lotto_generator = input("Press 'y' to create 6 random lottery numbers (1-50), or any other key to exit: ")

else:
    print("Thank you for using the Lotto Number Generator")
