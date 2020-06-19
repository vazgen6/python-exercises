# This assignment is based on Exercise 8.4 from your textbook.
# Each of the following Python functions is supposed to check whether its argument has any lowercase letters.
# For each function, describe what it actually does when called with a string argument.
# If it does not correctly check for lowercase letters,
# give an example argument that produces incorrect results,
# and describe why the result is incorrect.


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# In the function any_lowercase1 above the `else` is indented incorrectly
# from the first time that `c.isLower()` results to False the else statement will run
# and return False and the function will be terminated and we don't want that to happend
# after only checking the first character only, in the string.


print(any_lowercase1("HeLLO"))  # False


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# There are many things wrong in this function
# This function will always return "True", not the boolean value True
# "True" in as a string.
# because instead of checking the character in the string we're checking 
# if the lowercase letter 'c' is lowercase, which will always result in returning the 
# string 'True.
# The second mistake is that again the else statement is placed in the wrong placed
# even if instead of 'c'.islower() c.islower() was called this function would still not
# work correctly.
# Also the string 'False' is being returned instead of the boolean value False

print(any_lowercase2("HELLO"))  # "True"



def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# In this version what's wrong is that the function continues looping even after
# finding a lowercase, so if the last letter is an uppercase and there were million 
# lowercases before it it would return False
# This function will only work if the last word was lowercase, but there are much
# better ways to do that.

print(any_lowercase3("HElLO"))  # False
print(any_lowercase3("HElLo"))  # True (becuase of the last character)


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# This version works correctly, it initializes a flag with False value
# and sets it to the previous value if the previous value was True or c.islower()'s 
# value if it's True.
# This is not written in a good way because we keep looping even after we find a lowercase
# character, for example if we had a very log string with 100 letters and the first character
# was a lowercase which is enough for us to return True it'd still continue looping over
# the 100 characters.

print(any_lowercase4("HELLO"))  # False
print(any_lowercase4("HElLo"))  # True
print(any_lowercase4("sHElLoS"))  # True


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# what's wrong here is that we're checking if a character is not lowercase
# and it is returning False when it finds an uppercase, so from the first uppercase character
# the function will return False and stop, which is wrong.
# this would only work if we have a string with all lowercase characters.
# but again there are better ways to check if a string has all lowercase characters.

# print(any_lowercase5("HELLO"))  # False
# print(any_lowercase5("hello"))  # True