# eate your own Python code examples that demonstrate each of the following.

# Example 1: Define a function that takes an argument.
# Call the function.
# Identify what code is the argument and what code is the parameter.


from datetime import datetime


def greet(name, times):  # Function parameters are `name` and `times`
    for _ in range(times):
        print('Hello', name)


greet('Vasken', 3)  # Arguments are 'Vasken' and 3

# Example 2: Call your function from Example 1 three times with different kinds of arguments:
# a value, a variable, and an expression.
# Identify which kind of argument is which.

greet('Vasken', 3)  # arguments' values are the string 'Vasken' and the number 3

name = 'CS 1101'
times = 5
# arguments' variables are name and times which contain 'CS 1101' and 5 values respectively
greet(name, times)

# here we have the 'ha' * 3 expression which will result in a new string with value of 'hahaha'
# and 10**2 which is 10^2 = 100
# this function call will print 'hahaha' 100 times
greet('ha' * 3, 10**2)

# Example 3: Create a function with a local variable.
# Show what happens when you try to use that variable outside the function.
# Explain the results.


def getAge(yearOfBirth):
    year = datetime.now().year  # we declare local variable year
    return year - yearOfBirth


myAge = getAge(1997)
print(myAge)  # 22

# print(year) # we try accessing the variable year
# NameError: name 'year' is not defined
# Here we get this error because this variable is only defined and accessable in the function body
# and we use it when calculating the age
# and we can't access it outside the function

# Example 4: Create a function that takes an argument. Give the function parameter a unique name.
# Show what happens when you try to use that parameter name outside the function.
# Explain the results.


# def fun(with):
#     print('I like coffee with', with)
# fun('Chocolate')
# Here python show the following error while trying to run it
# SyntaxError: invalid syntax
# and it is correct because `with` is a reserved keyword by python
# and in order to make the function run correctly we can simply replace it
# with and other word that's not reserved

# Example 5: Show what happens when a variable defined outside a function
# has the same name as a local variable inside a function.
# Explain what happens to the value of each variable as the program runs.

name = 'Vasken'


def sayMyName():
    name = 'Jack Black'
    # here it always prints 'Jack Black' by accessing the locally created variable
    print(name)


sayMyName()

# Here it will print 'Vasken' by accessing the globally declared variable
print(name)

# conclusion:
# Even though we have two variables with the same name and before we print name in the last line
# we are changing its value in the function (assigning 'Jack Black' to it)
# this doesn't affect the variable declared globally which has the value of 'Vasken'


# Additional examples

########################################
# The code in this example is incorrect 
# because we are referncing the local variable name before assignment
# name = 'Vasken'

# def sayMyName2():
#     print(name)
#     name = 'Jack Black'
#     print(name)


# sayMyName2()
# print(name)
########################################

########################################
# The code in this example is correct 
# because here we are not declaring and new variable called name
# so Python will reference to the globally delcared variable called name
name = 'Vasken'

def sayMyName3():
    print(name)


sayMyName3()
print(name)

# Output:
# Vasken
# Vasken
########################################

# Learning Journal