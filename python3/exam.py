
numFriendCorrect = int(input())

friendAnswers = input()
myAnswers = input()

matchCount = 0
missMatchCount = 0
for i in range(len(myAnswers)):
    if myAnswers[i] == friendAnswers[i]:
        matchCount += 1
    else:
        missMatchCount += 1

if matchCount <= numFriendCorrect:
    possibleCorrectMatch = matchCount
    remainderCorrect = numFriendCorrect - matchCount
else:
    possibleCorrectMatch = numFriendCorrect
    remainderCorrect = matchCount - numFriendCorrect

numLeftOver = len(myAnswers)-possibleCorrectMatch
possibleCorrectLeftOver = numLeftOver - remainderCorrect

possibleCorrect = possibleCorrectMatch+possibleCorrectLeftOver
print(possibleCorrect)