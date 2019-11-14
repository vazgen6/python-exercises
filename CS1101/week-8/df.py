# Catching exceptions is a strong feature in Python that helps us prevent run-time errors and prevent the program from crashing or showing intimidating errors to users that won't have a clue of what had happened.

# Here are few examples or errors that we might do:

# Opening a file that doesn't exist
import os
file = open('file1.txt', 'r') # we are trying to open a file for reading that doesn't exist yet.

# Output Error:
# Traceback (most recent call last):
#   File "tmp.py", line 14, in <module>
#     file = open('file1.txt', 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'file1.txt'

# We can fix a situation like this by adding a try-except block

# Traceback (most recent call last):
#   File "tmp.py", line 14, in <module>
#     file = open('file1.txt', 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'file1.txt'

# We can fix a situation like this by adding a try-except block

try:
    file = open('file1.txt')
except FileNotFoundError: # we are prepared and excepting such an error
    # we can either inform the user that we were unable to find the file
    print("Couldn't find file")
    file = open('file1.txt', 'w')  # or we can create a new file

# Even a better solution would have been if we checked the file's existence before opening it

if (os.path.exists('file2.txt')): # if file exists we open it
    file = open('file2.txt')
    pass
else:
    print('file not found') # we can create a file or just skip reading it


# Creating a directory that already exists
import os

directory_name = 'Music'

try:
    os.makedirs(directory_name)
except FileExistsError:
    print('Directory {} already exists'.format(directory_name))

# In the case above I already had a folder called "Music" in my home directory and I was trying to create a new one, but Python threw an error `FileExistsError`

# Output of the error:

# Traceback (most recent call last):
#   File "tmp.py", line 3, in <module>
#     os.makedirs('Music')
#   File "/usr/lib/python3.6/os.py", line 220, in makedirs
#     mkdir(name, mode)
# FileExistsError: [Errno 17] File exists: 'Music'

# But I was able to handle the error above with the try-except blocks

# Removing a directory that does not exist
import os

to_delete = 'Music' # file/directory name to delete

try:
    os.remove(to_delete) # we try removing it, but it is not a file, so os.remove won't work
except IsADirectoryError:
# We print few warnings
    print('{} is a direcotory'.format(to_delete))
    print('using os.rmdir() instead')
    try:
# Now we try removing it as a directory
        os.rmdir(to_delete)
    except FileNotFoundError:
# not really possible after the steps above but I just added this except to be prepared just in case another program deleted the directory before us
        print('Directory does not exist')

# Of course the above examples could have been done with better code practices for example by doing simple checks before reading/deleting a file with the methods of os modules.


# In production we might have programs that need to be running 24/7 so we should be prepared for errors, a simple error should crash the program and terminate it.

# We must be able to handle errors and take necessary actions, so users that are relying on our program don't wait for hours before we know about it and re-run or fix it.

# Also in production it's always a good idea to log all errors in a file, working with files is so simple with Python like we have seen this week and it should take long lines of code to have a function that logs errors to a file, so later when a crash or error happens we can come back to the logs file and see what went wrong.

# References:
# Downey, A. (2015). Think Python, How to think like a computer scientist. 