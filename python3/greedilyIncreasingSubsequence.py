
maximum = int(input())
sequence = input().split()
sequence = [int(x) for x in sequence]

greadilyIncreasing = []
maxFound = sequence[0]
greadilyIncreasing.append(maxFound)
for i in range(1, len(sequence)):
    value = sequence[i]
    if value > maxFound:
        maxFound = value
        greadilyIncreasing.append(maxFound)
    if maxFound == maximum:
        break

print(len(greadilyIncreasing))
for v in greadilyIncreasing:
    print(v, end=' ')
print()

    
