# Note: You can skip the first part, I just explain here the basics about tuples.

# Tuples are pretty much like lists, except the big difference is, that tuples are immutable. This means that we can't modify its elements values, however we can reassign a tuple's value.

# For example:

my_tuple = (1, 2, 3)
my_tuple = (1, 2, 4)  # ✅ Allowed reassigning
# my_tuple[0] = 0  # ❌ Mutating is forbidden

# We can do almost all operations we can do with lists

# For example:

my_tuple = (1, 2, 3, 4)
my_tuple[0]  # 1
my_tuple[:2]  # (1,2)
my_tuple + (5, 6)  # (1,2,3,4,5,6)
(1, 2, 3) * 2  # (1,2,3,1,2,3)

# Also we can create tuples without parentheses, whenever Python sees multiple values separated by commas like the following 👇 it will pack them into a tuple:

tuple_var1 = 1, 2, 3
tuple_var2 = 'a', 'b', 'c'  # also a tuple

# Jump here 👋🏻 if you skipped the basics.

# So the big advantage of tuples in my opinion is that they are immutable and it's not easy to change its value by accident, when we assign its value we are sure that it's not changed somewhere and unlike dictionaries they are always in the same order.

# For example:

fruits = ('apples', 'oranges', 'bananas')
prices = (5, 6, 10)
for fruit, price in zip(fruits, prices):
    print('the price of {} is {}'.format(fruit, price))

# We create two tuples, I could also use arrays, but since I want to protect my fruits and prices variables from being mutated somewhere in future I put them in a tuple.

# And we loop over them both at the same time, by using zip to interleave them it will (note that if one tuple was longer than the other, the zip function will always zip by the length of the shorter tuple, same applies when working with arrays).

# We can also use the function enumerate with for loops to traverse the indices and its values for example:

friends = 'Pheobe', 'Joey', 'Chandler', 'Ross', 'Monica', 'Rachel'
for index, name in enumerate(friends):
    print('the index of {}, in friends list is {}'.format(name, index))

# Output:
# the index of Pheobe, in friends list is 0
# the index of Joey, in friends list is 1
# the index of Chandler, in friends list is 2
# the index of Ross, in friends list is 3
# the index of Monica, in friends list is 4
# the index of Rachel, in friends list is 5


# The items method of dictionaries can be used to iterate and it will return key value items in a tuple, example:
doctors = {'Lenoard': True, 'Sheldon': True, 'Raj': True,
           'Bernadetee': True, 'Amy': True, 'Howard': False}
for name, is_doctor in doctors.items():
    if is_doctor:
        print('{} is a doctor'.format(name))
    else:
        print('{} is not a doctor'.format(name))

# In case we didn't use .items() method to create tuples and iterate one at a time we would have to do something like this
# which is obviously less readable and not as efficient as the example above, of course there might be other ways also for achieving the same output but I see using items # method the most useful.
names = list(doctors.keys())
areDoctors = list(doctors.values())

for i in range(len(names)):
    if areDoctors[i]:
        print('{} is a doctor'.format(names[i]))
    else:
        print('{} is not a doctor'.format(names[i]))
# Output:
# Leonard is a doctor
# Sheldon is a doctor
# Raj is a doctor
# Bernadette is a doctor
# Amy is a doctor
# Howard is not a doctor
