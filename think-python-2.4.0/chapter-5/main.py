# Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
# a^n + b^n = c^n


def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print(a, b, c, n)
        print('Holy smokes, Fermat was wrong!')
    else:
        pass
        # print('No, that doesn’t work.')


# for i in range(1, 100):
#     for j in range(1, 100):
#         for k in range(1, 100):
#             for y in range(3, 100):
#                 check_fermat(i, j, k, y)


# def is_triangle(a, b, c):
#     if (a > c + b
#         or b > a + c
#             or c > b + a):
#         print('No')
#     else:
#         print('Yes')


# is_triangle(9, 10, 11)
# is_triangle(4, 1, 1)
# is_triangle(6, 6, 6)

# print('123'.isnumeric())


# my_var = input('Enter a number: ')

# if not my_var.isnumeric():

#     print('Invalid number')

# elif int(my_var) % 2 == 0:

#     print(my_var, 'is even number')

# else:

#     print(my_var, 'is odd number')


user_age = input("enter your age: ")
if int(user_age) > 16:
    cs_student = input("do you study computer science ? (y/n) ")
    if cs_student == 'y':
        print('You rock!')
    else:
        print('You should join UoPeople')
else:
    print('not allowed')
