prefixes = 'JKLMNOPQ'
suffix = 'ack'
specialCases = ['O', 'Q']
for letter in prefixes:
    if letter in specialCases:
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# examples that show different features of string slices.
my_string = 'hello, world'

# Example 1
# In this example we slice the string and keep only the first 5 characters
# if we don't provide the first index it will start from 0
# so the two examples below are the same
print(my_string[:5])  # hello
print(my_string[0:5])  # hello

# Example 2
# In this example we slice the string and keep only the last 5 characters (world)
# if we don't provide the second index it will go until the end of the string
# so the two examples below are the same
print(my_string[7:])  # world
print(my_string[7:12])  # world


# Example 3
# In this example we make a copy using slice
print(my_string[:])  # hello, world

# Additional examples
# Invalid indexes, the starting index should be less than the end
# these will return an empty string ''
print(my_string[5:3])
print(my_string[5:5])
