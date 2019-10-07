# As an exercise, write a function that takes a string
# as an argument and displays the letters backward, one per line.

def printBackwars(str):
    index = len(str) - 1
    while index > -1:
        print(str[index])
        index = index - 1

printBackwars('')