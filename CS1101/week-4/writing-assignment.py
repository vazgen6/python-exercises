# Exercise 6.4.
# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b
# and returns True if a is a power of b .
# Note: you will have to think about the base case.


def is_divisible(x, y):
    # easy check, if the reminder is zero then it's divisible,
    # the function will return a boolean value
    return x % y == 0


def is_power(a, b):
    if a == b:  # base case where a/b == 1
        return True
    elif b == 1:  # base case where b == 1 but a does not
        return False
    else:
        return is_divisible(a, b) and is_power(a/b, b)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
