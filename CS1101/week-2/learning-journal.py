# Part 1

# The volume of a sphere is 4/3πr3, where π has the value of "pi" given in Section 2.1 of your textbook.
# Write a function called print_volume (r) that takes an argument for the radius of the sphere, and prints the volume of the sphere.

# Call your print_volume function three times with different values for radius.

# Include all of the following in your Learning Journal:

#     The code for your print_volume function.
#     The inputs and outputs to three calls of your print_volume.

from math import pi  # We Import pi from math module to use it later in the function


def print_volume(r):
    # We do a quick check to see if we are getting a positive number
    if (r < 1):
        return print('radius must be positive number')
    print('The Volume is', round(4 / 3 * pi * r ** 3, 4))


# Input (argument): 0, invalid input will print an error message
print_volume(0)
print_volume(-5)  # Input: -5, again invalid input will print an error message
print_volume(6)  # Input: 6, valid input, will print 904.7787

# We can get inputs from the user too!
for _ in range(3):  # let's call it three times
    usr_input = input('Enter radius: ')
    # float(usr_input) to convert from string to float
    if (usr_input.isnumeric()):  # we check if user entered only numbers so float() doesn't throw an error
        print_volume(float(usr_input))
    else:
        print('Invalid Input!')

# Part 2

# Write your own function that illustrates a feature that you learned in this unit.
# The function must take at least one argument. The function should be your own creation,
# not copied from any other source. Do not copy a function from your textbook or the Internet.

# Include all of the following in your Learning Journal:

#     The code for the function that you invented.
#     The inputs and outputs to three calls of your invented function.
#     A description of what feature(s) your function illustrates.


# I decided to write a simple average calculator function
# it takes a list and calculates the average of the elements
# I call it first with a list with three elements
# second time with no elements
# third time I let the user input the elements


def average_calculator(nums):
    if (isinstance(nums, list) and len(nums)):
        sum = 0
        for num in nums:
            sum += num
        avg = sum / len(nums)
        print('Average:', round(avg, 2))
        return avg


# Here we pass an array with three numbers (grades) and it prints the average
average_calculator([10, 10, 9])  # Output: 9.67

# Here we pass an empty list and the function does nothing
average_calculator([])

# In this example we let the user input
print('\n\nThis program calculates the average of your grades.\nType "stop" to stop')
nums = []
usr_input
while(usr_input != 'stop'):
    usr_input = input('Enter Grade: ')
    if (usr_input != 'stop' and usr_input.isnumeric()):
        nums.append(float(usr_input))

average_calculator(nums)
