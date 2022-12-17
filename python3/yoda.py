
first = input()
second = input()
first = [int(l) for l in first]
second = [int(l) for l in second]
first.reverse()
second.reverse()

maximumLength = max(len(first), len(second))
while len(first) < maximumLength:
    first.append(0)
while len(second) < maximumLength:
    second.append(0)

firstResult = ""
secondResult = ""
for i in range(maximumLength):
    a = first.pop()
    b = second.pop()
    if a > b:
        firstResult += str(a)
    elif b > a:
        secondResult += str(b)
    else:
        firstResult += str(a)
        secondResult += str(b)

if firstResult == '':
    print("YODA")
else:
    print(int(firstResult))
if secondResult == '':
    print("YODA")
else:
    print(int(secondResult))

