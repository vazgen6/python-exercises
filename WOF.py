VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
import random
# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self, name)
    def getMove(self, category, obscuredPhrase, guessed):
        print('{} has ${}\n'.format(self.name, self.prizeMoney))
        
        print('Category: {}'.format(category))
        print('Phrase: {}'.format(obscuredPhrase))
        print('Guessed: {}\n'.format(guessed))
        
        return input("Guess a letter, phrase, or type 'exit' or 'pass': ")
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFHumanPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        WOFHumanPlayer.__init__(self, name)
        self.difficulty = difficulty
        
    def smartCoinFlip(self, a):
        return random.randint(1, 10) > self.difficulty
    
    def getPossibleLetters(self, guessed):
        newList = []
        for l in LETTERS:
            if l not in guessed:
                newList.append(l)
        if self.prizeMoney < VOWEL_COST:
            finalList = []
            for i in newList:
                if i not in VOWELS:
                    finalList.append(i)
            return finalList
        else:
            return newList

    def getMove(self, category, obscuredPhrase, guessed):
        possibleLetters = self.getPossibleLetters(guessed)
        # print(possibleLetters)
        if len(possibleLetters) == 0:
            return 'pass'
        else:
            if self.smartCoinFlip(possibleLetters):
                return possibleLetters[-1]
            else:
                return random.choice(possibleLetters)
