import math

# part 1:


def my_sqrt(a):

    x = a-1

    while True:

        y = (x + a/x) / 2.0

        if y == x:

            break

        x = y

    return y


print(my_sqrt(4))

# Modify your program so that it outputs lines for a values from 1 to 25 instead of just 1 to 9.


# from 1 to 25

def test_sqrt():

    while True:

        for a in range(1, 25):  # can not assign (1) to (a) because we ca not devide to zero

            diff = my_sqrt(a) - math.sqrt(a)

            print('my_sqrt({}) ='.format(a), my_sqrt(a), 'math.sqrt(a) =|',
                  math.sqrt(a), ' diff =', diff)

        return


test_sqrt()
