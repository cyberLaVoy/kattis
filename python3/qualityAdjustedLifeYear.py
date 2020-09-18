import sys

numberOfPeriods = int(sys.stdin.readline())

accumulatedQALY = 0
for i in range(numberOfPeriods):
    line = sys.stdin.readline().strip().split(' ')
    quality = float(line[0])
    quantity = float(line[1])
    accumulatedQALY += (quality*quantity)

print(accumulatedQALY)

