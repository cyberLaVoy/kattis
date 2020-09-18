import math

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
circle = {}
for l in letters:
    circle[l] = ord(l) - 65
circle[' '] = 26
circle["'"] = 27

numAphorisms = int(input())

letterDistance = 60*math.pi/28 # feet between each letter
playerSpeed = 15 # feet per second 
for i in range(numAphorisms):
    aphorism = input()
    timeTaken = 1
    for j in range(1, len(aphorism)):
        currLetter = aphorism[j-1]
        nextLetter = aphorism[j]
        distCounterClockwise = abs(circle[currLetter]-circle[nextLetter])
        distClockwise = 28 - distCounterClockwise
        timeTaken += min(distClockwise, distCounterClockwise)*letterDistance/playerSpeed
        timeTaken += 1
    print(timeTaken)



