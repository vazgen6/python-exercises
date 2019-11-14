
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle',
                                    'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]


def findWord(arr, word):
    for i in arr:
        if type(arr[0]) == list:
            foundWord = findWord(i, word)
            if foundWord:
                return foundWord
        else:
            if word in i:
                return word


output = findWord(nested, 'snake')

print(output)
