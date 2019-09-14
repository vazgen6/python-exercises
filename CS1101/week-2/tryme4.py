# just prints a dot then jumps into a new line
def new_line():
    print('.')

# prints three dots, each on a new line
def three_lines():
    new_line()
    new_line()
    new_line()

# in this function we call three_lines() three times so we get nine lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
    # we could do it the following way too
    # for _ in range(3)
    #   three_lines()

# uses a combination of the functions nine_lines, three_lines, and new_line (provided below) to print a total of twenty-five line
def clear_screen():
    nine_lines() # 9
    nine_lines() # 9
    three_lines() # 3
    three_lines() # 3
    new_line()    # 1
            # Total = 25  


print('Printing nine lines') # a message so it's clear that we are calling nine_lines after this
nine_lines() # calling the function
print('Calling clear_screen()') # a message so it's clear that we are calling clear_screen after this
clear_screen() # calling the function
