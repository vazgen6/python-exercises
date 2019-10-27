alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz", "dog", "bookkeeper",
             "subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz", "subdermatoglyphic",
             "the quick brown fox jumps over the lazy dog"]


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# Part 1
def has_duplicates(s):
    my_dict = histogram(s)
    for c in my_dict.values():
        if c > 1:
            return True
    return False


for s in test_dups:
    print('{} has{} duplicates'.format(s, '' if has_duplicates(s) else ' no'))

print('\n\n')
# Part 2 

def missing_letters(s):
    global alphabet
    my_dict = histogram(s)
    missing_letters_str = ''
    for c in alphabet:
        if c not in my_dict:
            missing_letters_str = missing_letters_str + c
    return missing_letters_str

for s in test_miss:
    missing_letters_str = missing_letters(s)
    if not len(missing_letters_str):
        print('{} uses all the letters'.format(s))
    else:
        print('{} is missing letters {}'.format(s, missing_letters_str))

# Output:
# zzz has duplicates
# dog has no duplicates
# bookkeeper has duplicates
# subdermatoglyphic has no duplicates
# subdermatoglyphics has duplicates



# zzz is missing letters abcdefghijklmnopqrstuvwxy
# subdermatoglyphic is missing letters fjknqvwxz
# the quick brown fox jumps over the lazy dog uses all the letters

# References:
# Downey, A. (2015). Think Python, How to think like a computer scientist.
