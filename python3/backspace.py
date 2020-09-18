
line = input()
line = [l for l in line]

newLine = []
for l in line:
    if l == '<':
        newLine.pop()
    else:
        newLine.append(l)

for l in newLine:
    print(l, end='')
print()
