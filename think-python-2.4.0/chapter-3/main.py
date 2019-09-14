# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the
# string is in column 70 of the display.


def rightJustify(str):
    paddCount = 70 - len(str)
    print(' ' * paddCount + str)


rightJustify('Hello')
rightJustify('Da')


# A function object is a value you can assign to a variable or pass as an argument.
# For example, do_twice is a function that takes a function object as an argument
# and calls it twice:

def doTwice(f, name):
    for _ in range(2):
        f(name)


def sayHello(name):
    print("hello", name)


doTwice(sayHello, "Vazgen")


# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def printCrazyShape():
    for _ in range(2):
        for _ in range(2):
            print('+', '- '*4, end = ' ')
        print('+')
        for _ in range(4):
            for _ in range(3):
                print('|', ' ' * 8,  end = ' ')
            print('')
    for _ in range(2):
        print('+', '- '*4, end = ' ')
    print('+')


printCrazyShape()
