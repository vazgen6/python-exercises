def is_divisible(a, b):                                     #this is the is_division function that which first inspects if arguments are divisible
    if a % b == 0:                                          #the modulous operator gives an output of a remainder in the argument; if zero return True
        return True
    else:                                                   #if arguments gives remainder the return is False
        return False

def is_power(a, b):                                         #the is_power function will return True if a is a power of b
    if is_divisible(a, b) == False:                         #arguments must match the True output of the is_divisible function; if false return false to program
        return False
    elif b == 1 or a == b:                                            #if  b is 1 program returns True
        return True
    elif a == b:                                            ##stops recursion when divison of powers is complete
        return True
    elif is_divisible(a, b) == True:                        #divides x by y and calls function again
        return is_power(a/b, b)

print('is_power(10, 2) returns: ', is_power(10, 2))
print('is_power(27, 3) returns: ', is_power(27, 3))
print('is_power(1, 1) returns: ', is_power(1, 1))
print('is_power(10, 1) returns: ', is_power(10, 1))
print('is_power(3, 3) returns: ', is_power(3, 3))