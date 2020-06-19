# Practice using the Python interpreter as a calculator:

# The volume of a sphere with radius r is 4/3πr^3 . 
# What is the volume of a sphere with radius 5?

from math import pi

r = 5
v = 4 / 3 * pi * r ** 3

print("The Volume is", round(v, 2))

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?

def calcDiscount(price, discount):
    return price - (price * discount) / 100

def calcShippingCosts(numberOfCopies):
    if (numberOfCopies == 1):
        return 3
    else:
        return (numberOfCopies - 1) * 0.75 + 3

total = round(calcDiscount(24.95, 40) * 60 + calcShippingCosts(60), 2)

print("The total wholesale cost for 60 copies is:", total)

