"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730397626"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
number = (randint(1, 4))

if number <= 2:
    if number != 1:
        print("Tomorrow will be your lucky day!")
    else:
        print("If you can dream it, you can beccome it!")
else: 
    if number == 3:
        print("Happiness ahead!")
    else:
        print("Be the change you want to see in the world!")

print("Now, go spread positive vibes!")