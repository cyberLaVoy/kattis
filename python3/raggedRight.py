import sys

line = sys.stdin.readline()
lines = []
maxLength = 0
while line != '':
    line = line.strip()
    if len(line) > maxLength:
        maxLength = len(line)
    lines.append(line)
    line = sys.stdin.readline()

lines.pop()
score = 0
for line in lines:
    score += (len(line) - maxLength)**2
print(score)
