
def lowerVersion(string):
    return string.lower()

def display(words):
    words.sort(key=lowerVersion)
    for i in range(len(words[0])):
        string = ""
        for j in range(len(words)):
            string += words[j][i]
        print(string)
    print()

def solve():
    params = input().split()
    wordLength = int(params[0])
    numWords = int(params[1])
    while not (wordLength==0 and numWords==0):
        words = [""]*numWords
        for i in range(wordLength):
            line = input()
            for j in range(numWords):
                words[j] += line[j]
        display(words)

        params = input().split()
        wordLength = int(params[0])
        numWords = int(params[1])
solve()