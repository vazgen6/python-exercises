# Part 1

# Write a Python program that does the following.

#     Create a string that is a long series of words separated by spaces.
# The string is your own creative choice.
# It can be names, favorite foods, animals, anything.
# Just make it up yourself. Do not copy the string from another source.

#     Turn the string into a list of words using split.

#     Delete three words from the list, but delete each one using a different kind of Python operation.

#     Sort the list.

#     Add new words to the list (three or more) using three different kinds of Python operation.

#     Turn the list of words back into a single string using join.

#     Print the string.

names = 'Pirlo Buffon Toni Gattuso Zambrotta Cannavaro Grosso Totti Materazzi Ronaldo Messi Modric Zidan'

list_of_words = names.split()

# remove not Italian names
list_of_words.remove('Ronaldo')  # using remove
index_zidan = list_of_words.index('Zidan')
list_of_words.pop(index_zidan)  # pops the elemt at the index passed
list_of_words.pop()  # last element
index_messi = list_of_words.index('Messi')
del list_of_words[index_messi]  # deletes element

# sort
list_of_words.sort()

# add new items
list_of_words.append('Del Piero')
list_of_words.extend(['De Rossi'])
list_of_words.insert(0, 'Barzagli')

new_names = " ".join(list_of_words)

print(new_names)


# Part 2

# Provide your own examples of the following using Python lists. Create your own examples. Do not copy them from another source.

#     Nested lists
#     The “*” operator
#     List slices
#     The “+=” operator
#     A list filter
#     A list operation that is legal but does the "wrong" thing, not what the programmer expects

# Provide the Python code and output for your program and all your examples.

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]

# The “*” operator
# With numbers
a = 5
b = 2
print(a * b)  # 10
a *= b
print(a)  # 10

# with strings
a = 'hello'
print(a*2)  # hellohello

# with lists
lst = [1, 2, 3]
print(lst*2)  # [1,2,3,1,2,3]


# The “+=” operator
a = 5
b = 10

a += b
print(a)  # 15

# A list filter


def filterIntegers(lst):
    new_list = []
    for item in lst:
        if type(item) is int:
            new_list.append(item)
    return new_list


filtered_list = filterIntegers(['potato', 1, 'bananas', 2, 'appels', 3])
print(filtered_list)  # [1, 2, 3]

# A list operation that is legal but does the "wrong" thing, not what the programmer expects

# a mistake that I did while learning was using the sort method in a wrong way
# I did
my_list = [5, 1, 2]
my_list_sorted = my_list.sort()  # ❌
print(my_list_sorted)  # None
# and expected to have a new list sorted in my_list_sorted variable
# but .sort() returns None and sorts the original list
# there are two solutions
# 1: if we want the original list to be sorted we can just remove the assignment
my_list = [5, 1, 2]
my_list.sort()
print(my_list)  # [1,2,5]

# 2: use the sorted method
my_list = [5, 1, 2]
my_list_sorted = sorted(my_list)
print(my_list_sorted)  # [1,2,5]


# Part 3

# Describe your experience so far with peer assessment of Programming Assignments.

# How do you feel about the aspect assessments and feedback you
# have received from your peers?

# In general everything is going really well and I am happy, like I said before I appriciate the feedback I get
# both negative and positive, it's an oppurtunity for me to learn more

# How do you think your peers feel about the aspect assessments and
# feedback you provided them?
# I always try to be helpful and make sure I understand student's work very well before assessing it
# I try to be helpful and point out the mistaks or ways they can improve their code.

