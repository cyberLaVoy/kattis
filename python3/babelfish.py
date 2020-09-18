
import sys

dictionary = {}
entry = sys.stdin.readline()
while entry != '\n':
    entry = entry.strip().split()
    dictionary[entry[1]] = entry[0]
    entry = sys.stdin.readline()

word = sys.stdin.readline()
while word != '':
    word = word.strip()
    if word in dictionary:
        print(dictionary[word])
    else:
        print("eh")
    word = sys.stdin.readline()

