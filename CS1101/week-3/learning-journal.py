# 1. Copy the countdown function from Section 5.8 of your textbook.
from time import sleep


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


# Write a new recursive function countup that expects a negative argument and counts “up” from that number.
# Output from running the function should look something like this:

# >> > countup(-3)
# -3
# -2
# -1
# Blastoff!


def countup(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        sleep(0.5)  # just to add some delay
        countup(n+1)


countup(-5)


# Write a Python program that gets a number using keyboard input.
# (Remember to use input for Python 3 but raw_input for Python 2.)
usr_input = input('Enter a number: ')

try:
    num = int(usr_input)
    if num > 0:  # when the number is positive
        countdown(num)
    else:   # when the number is negative or zero
        countup(num)
except ValueError:
    print('Invalid input')

# Output
# Enter a number: 5
# 5
# 4
# 3
# 2
# 1
# Blastoff!

# Enter a number: -3
# -3
# -2
# -1
# Blastoff!

# Enter a number: 0
# Blastoff!


# An explanation of your choice for what to call for input of zero.
# I call countdown when I have positive numbers and in the else block countup is called,
# when we have negative numbers of zero.

# 2. Write your own unique Python program that has a runtime error.
# Do not copy the program from your textbook or the Internet. Provide the following.

# The code of your program.
# my_var = 'elephant'
# int(my_var)

# Output demonstrating the runtime error, including the error message.
# Traceback (most recent call last):
#   File "learning-journal.py", line 76, in <module>
#     int(my_var)
# ValueError: invalid literal for int() with base 10: 'elephant'

# An explanation of the error message.
# So what is happening here is a mistake I made on purpose, I tried converting a string to an integer
# which is not possible that's why we got a runtime error.

# An explanation of how to fix the error.
# We can handle this by using try - except blocks like I used in the first exercise above
# Or we just simple replace the value of my_var to any other valid string that contains numbers only.
def fun:
    print('hi')
print(fun())