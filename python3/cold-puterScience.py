import sys

sys.stdin.readline()

temps = sys.stdin.readline().strip().split(' ')

totalDays = 0
for temp in temps:
    if int(temp) < 0:
        totalDays += 1
print(totalDays)

