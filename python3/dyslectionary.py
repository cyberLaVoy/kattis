import sys

def printDyslectionary(words, longestWord):
    words.sort()
    for word in words:
        paddingLength = longestWord - len(word)
        padding = ' '*paddingLength
        print(padding+word[::-1])

def parseInput():
    words = []
    longestWord = 0
    for word in sys.stdin:
        word = word.strip()
        if word == '':
            printDyslectionary(words, longestWord) # print each collection of words, before last collection
            print()
            words = []
            longestWord = 0
        else:
            words.append(word[::-1])
            if len(word) > longestWord:
                longestWord = len(word)
    printDyslectionary(words, longestWord) # print the last collection of words
parseInput()