
params = input().split()
roomWidth = int(params[0])

partitions = input().split()
roomLines = [0]
for part in partitions:
    roomLines.append(int(part))
roomLines.append(roomWidth)

widths = []
for i in range(len(roomLines)):
    start = roomLines[i]
    for j in range(i+1, len(roomLines)):
        end = roomLines[j]
        width = end-start
        widths.append(width)

widths = list(set(widths))
widths.sort()
for width in widths:
    print(width, end=' ')
print()


