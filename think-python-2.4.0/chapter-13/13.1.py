# Write a program that reads a file, breaks each line into words,
# strips whitespace and punctuation from the words, and converts them to lowercase.
from string import punctuation, whitespace

with open('random.txt') as file:
    for line in file:
        words = line.split()
        cleanedWords = []
        for word in words:
            cleandWord = word
            for c in punctuation:
                cleandWord = cleandWord.replace(c, '')
            cleanedWords.append(cleandWord)
        print(cleanedWords)
