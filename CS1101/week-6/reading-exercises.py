# Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists. For example:

# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21


def nested_sum(arr):
    total = 0
    if type(arr) is list:
        for n in arr:
            if(type(n) is list):
                total += nested_sum(n)
            else:
                total += n
        return total


print(nested_sum([[1, 2], [3], [4, 5, 6], 1]))


# Exercise 10.2. Write a function called cumsum that takes a list of
# numbers and returns the cumulative sum; that is, a new list where
# the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

def cumsum(t):
    arr = []
    total = 0
    for i in t:
        total += i
        arr.append(total)
    return arr


t = [1, 2, 3]
print(cumsum(t))


# Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]
def middle(t):
    return t[1:len(t) - 1]


t = [1, 2, 3, 4]
print(middle(t))
# [2, 3]


# Exercise 10.4. Write a function called chop that takes a list,
# modifies it by removing the first and
# last elements, and returns None . For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]

def chop(t):
    del t[0]
    del t[len(t) - 1]


t = [1, 2, 3, 4]
chop(t)
print(t)

# Exercise 10.5. Write a function called is_sorted
# that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise.
# For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False


def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            return False
    return True


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))


# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are
# anagrams.

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.

def has_duplicates(s):
    for c in s:
        if s.count(c) > 1:
            return True
    return False

print(has_duplicates('abc'))
print(has_duplicates('abbc'))


# This exercise pertains to the so-called Birthday Paradox, which you can read about
# at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
# If there are 23 students in your class, what are the chances 
# that two of you have the same birthday?
# You can estimate this probability by generating random 
# samples of 23 birthdays and checking for
# matches. Hint: you can generate random birthdays 
# with the randint function in the random
# module
from random import randint
student_ages = []
for i in range(23):
    student_ages.append(randint(1, 365))
