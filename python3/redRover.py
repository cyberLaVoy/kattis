
directions = input()
shortestLength = len(directions)
for i in range(len(directions)):
    for j in range(i+2,len(directions)+1):
        section = directions[i:j]
        encoded = directions.replace(section, 'M')
        length = len(section) + len(encoded)
        shortestLength = min(length, shortestLength)
print(shortestLength)

