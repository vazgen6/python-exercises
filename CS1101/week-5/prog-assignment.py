from math import sqrt


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return y


def test_sqrt():
    i = 1
    while i < 26:
        my_sqrt_val = my_sqrt(i)
        math_sqrt_val = sqrt(i)
        print("a = {} | my_sqrt(a) = {} | math.sqrt(a) = {} | diff = {}"
              .format(i, my_sqrt_val, math_sqrt_val, my_sqrt_val - math_sqrt_val))
        i += 1


test_sqrt()
