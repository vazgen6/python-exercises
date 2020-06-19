import turtle
from math import pi

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360 / n)


def circle(t, r):
    circumference = 2 * pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)


bob = turtle.Turtle()
# square(bob, 100)
# square(bob, 500)
# polygon(bob, 100, 8)
circle(bob, 100)
turtle.mainloop()
