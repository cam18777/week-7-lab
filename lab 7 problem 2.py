# camryn echevarria
# 11/28/2022

# Problem 2 is to write a function that shows a number between 1 and 10 to see if it's true or flase.

# to see witch number picked random is true that its between 1-10
import random
def check_range():
    # check if number is in the range of 1 - 10
    if 1 <= input_number <= 10:

        print(True)
    # if number isn't within range than it is outside the range
    else:

        print(False)

number = int(input("What is your number?\n"))
# assign input into created function
check_range(number)

print(check_range(1, 11))


check_range()