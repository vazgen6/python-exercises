# In many high level languages such as Python almost everything is an object and objects have ids.

# Let's take the following example with numbers

a = 5
b = 5
id(a) # 1
id(b) # 1
a is b # True (identical) ✅
a == b # True (equivalent) ✅

# In the example above we declared two variables a and b by default Python is smart enough to see that these two variables share the same value so it doesn't allocate separate memory for each and makes them share the same place in the memory.
# So these two variables are equivalent (have the same value) and identical (point to the same place in memory and are the same object).
# In order to see the unique id of each variable you can use the id function and it will return the id of the variable in memory in this case since both are identical. (The number 1 was a random number by me this will be always be different). The case is the same with strings.

# But with lists it works differently

a = [1, 2, 3]
b = [1, 2, 3]
id(a) # 1
id(b) # 2
a is b # False (not identical) ❌
a == b # True (equivalent) ✅

# In the example above you see that we have two lists (a and b) with same values. Python allocated separate spaces for them in memory although in this case they are equivalent (have the same values) they are not identical (are not the same object so don't point to the same location in memory).

# Lists also can be identical, for example:

a = [1, 2, 3]
b = a
id(a) # 1
id(b) # 1
a is b # True (identical) ✅
a == b # True (equivalent) ✅

# mutating
a.append(4)
a # [1,2,3,4]
b # [1,2,3,4]
a is b # True (identical) ✅
a == b # True (equivalent) ✅
# assigning (creating)
a = [1,2,3,4,5]
a # [1,2,3,4,5]
b # [1,2,3,4]
a is b # (not identical) ❌
a == b # (not equivalent) ❌
b = [1,2,3,4,5]
a is b # (not identical) ❌ still are not identical
a == b # (equivalent) ✅ now have the same values

# You can see this example is similar the one above but instead of creating a new list for b I assigned a to it and now these objects are identical, if we try and mutate any of them for example the a.append(4) this will make both lists get the value 4 added because they point to the same memory and are the same object so any mutations to one of them will result in changes in the other.

# But when we use the assignment operator to assign (create) a new list, this relation between them is deleted and they are no longer identical they can be equivalent and still have the same value, but they're no longer sharing the same object and place in memory. We can make them identical again by using the assignment operator we used in first place by doing
# a = b again.

# Example of a function that modifies a list passed in as an argument

def mulByTwo(lst):
  for i in range(len(lst)):
      lst[i] = lst[i] * 2
a = [1,2,3]
mulByTwo(a)
a # [2,4,6]

# This is a simple function that takes a list of integers as an argument and multiplies each by two. First we create a new list a = [1, 2, 3] then we call mulByTwo and pass a as argument this will pass its reference and not a copy of it. The function will modify the passed list so as you can see after the function call the values of the items of the list are changed.

# References:
# Downey, A. (2015). Think Python, How to think like a computer scientist. 