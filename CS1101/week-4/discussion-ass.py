# The precondition


def sum1(num1, num2):
    return num1 + num2


# Voilating precondition, the function is designed to
# sum two integers but we are passing one stirng and one number
# sum1('5', 5)


def sum2(num1: int, num2: int):
    return num1 * num2


# Voilating postcondition, the function is designed to
# sum two integers but instead it's multiplying them
# all passed arguments are correct and there's no precondition violation
sum2(1, 2)


# this one checks for the arguments being passed to be numbers
def sum3(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return print(num1 * num2)


# Here we have two violations, precondition and postcondition , the function is designed to
# sum two integers and return the sum but instead it's printing the sum directly
# and returning the return value of the function print which is the value None
# then in the function call we are adding 5 to the returned value 5
# which will cause an error
s = 4
print(sum3(5, 5) + 5)
