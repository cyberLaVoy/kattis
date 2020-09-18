

def numLettersAwayFromPer(subWord):
    per = "PER"
    lettersAway = 0
    for i in range(len(subWord)):
        if subWord[i] != per[i]:
            lettersAway += 1
    return lettersAway

def solveConundrum():
    word = input()
    totalDays = 0
    for i in range(0,len(word)-2,3):
        subWord = word[i:i+3]
        totalDays += numLettersAwayFromPer(subWord)
    print(totalDays)
solveConundrum()
