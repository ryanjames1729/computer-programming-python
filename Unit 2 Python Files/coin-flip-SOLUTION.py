# CDS - Programming
# Coin Flip Assignment
#
# Student Name: TEACHER SOLUTION

# import libraries
from random import randint

# Pick a random number: either 0 or 1
rand = randint(0,1)

# Determine the flip
coinFlip = ""
if rand == 0:
    coinFlip = "Heads"
elif rand == 1:
    coinFlip = "Tails"

# Print the output
print("The coin is flipped...and it is {}!".format(coinFlip))