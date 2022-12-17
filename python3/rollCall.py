import sys

def lastName(name):
    return name[1] + name[0]

names =[]
firstNames = {}
firstNamesDup = {}
name = sys.stdin.readline().strip()
while name != '':
    name = name.split()
    names.append(name)
    if name[0] in firstNames:
        firstNamesDup[name[0]] = 1
    firstNames[name[0]] = 1

    name = sys.stdin.readline().strip()

    
for name in names:
    if name[0] in firstNamesDup:
        name.append(1)
    else:
        name.append(0)
        
names.sort(key=lastName)
for name in names:
    if name[2]:
        print(name[0], name[1])
    else:
        print(name[0])

        